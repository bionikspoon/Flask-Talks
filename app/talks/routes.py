# coding=utf-8
from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from . import talks
from .. import db
from .forms import ProfileForm
from ..models import User


@talks.route('/')
def index():
    return render_template('talks/index.html')


@talks.route('/user/<username>')
def user(username):
    user_ = User.query.filter_by(username=username).first_or_404()
    return render_template('talks/user.html', user=user_)


@talks.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()

        flash('Your profile has been updated.', category='success')
        return redirect(url_for('talks.user', username=current_user.username))

    form.name.data = current_user.name
    form.location.data = current_user.location
    form.bio.data = current_user.bio
    return render_template('talks/profile.html', form=form)