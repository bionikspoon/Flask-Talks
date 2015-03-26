# coding=utf-8
from flask import (render_template, flash, redirect, url_for, request,
                   current_app)
from flask.ext.login import login_user, logout_user, login_required

from ..models import User
from . import auth
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    unsecured_live = all((
        not current_app.config['DEBUG'], not current_app.config['TESTING'],
        not request.is_secure))
    if unsecured_live:
        return redirect(url_for('.login', _external=True, _scheme='https'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('.login'))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('talks.index'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('talks.index'))