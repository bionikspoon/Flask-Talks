# coding=utf-8
from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from . import talks
from .. import db
from .forms import ProfileForm, TalkForm
from ..models import User, Talk


@talks.route('/')
def index():
    talk_list = Talk.query.order_by(Talk.date.desc()).all()
    return render_template('talks/index.html', talks=talk_list)


@talks.route('/user/<username>')
def user(username):
    user_ = User.query.filter_by(username=username).first_or_404()
    talk_list = user_.talks.order_by(Talk.date.desc()).all()
    return render_template('talks/user.html', user=user_, talks=talk_list)


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


@talks.route('/new', methods=['GET', 'POST'])
@login_required
def new_talk():
    form = TalkForm()
    if form.validate_on_submit():
        talk = Talk(title=form.title.data, description=form.description.data,
                    slides=form.slides.data, video=form.video.data,
                    venue=form.venue.data, venue_url=form.venue_url.data,
                    date=form.date.data, author=current_user)
        db.session.add(talk)
        db.session.commit()
        flash('The talk was added successfully.', category='success')
        return redirect(url_for('.index'))
    return render_template('talks/edit_talk.html', form=form)
