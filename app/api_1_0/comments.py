# coding=utf-8
from flask import jsonify, g

from . import api
from .errors import bad_request, forbidden
from .. import db
from ..models import Comment


# noinspection PyShadowingBuiltins
@api.route('/comments/<int:id>', methods=['PUT'])
def approve_comment(id):
    comment = Comment.query.get_or_404(id)
    can_modify_requirements = (
        not comment.talk.author == g.current_user, not g.current_user.is_admin)
    if all(can_modify_requirements):
        return forbidden('You cannot modify this comment.')
    if comment.approved:
        return bad_request('Comment is already approved.')
    comment.approved = True
    db.session.add(comment)
    db.session.commit()
    return jsonify(dict(status='ok'))


# noinspection PyShadowingBuiltins
@api.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    if comment.talk.author != g.current_user and not g.current_user.is_admin:
        return forbidden('You cannot modify this comment.')
    if comment.approved:
        return bad_request('Comment is already approved.')
    db.session.delete(comment)
    db.session.commit()
    return jsonify(dict(status='ok'))