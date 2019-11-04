# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash, request, session, make_response
from contrs.main import main
from config import db
from models.users import User
from models.roles import Role
from models.roles import Perm
from contrs.main.forms import EditProfileForm, EditProfileAdminForm
from flask_login import login_required, current_user
from contrs.decorators import permission_required, admin_required
import json


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/json', methods=['GET', 'POST'])
def send_json():
    ss = {'a': 'qwer'}
    return json.dumps(ss)


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return 'For administrators!'


@main.route('/moderator')
@login_required
@permission_required(Perm.M)
def for_moderators_only():
    return 'For moderators!'


@main.route('/user-info/<username>')
def user_info(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user_info.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user_info', username=current_user.username))
    form.name.data = current_user.username
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(user_id):
    user = User.query.get_or_404(user_id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('The profile has been updated.')
        return redirect(url_for('.user_info', username=user.username))
    form.username.data = user.username
    form.email.data = user.email
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)
