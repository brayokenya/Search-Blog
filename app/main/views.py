from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm, UpdateProfile
from flask_login import login_required, current_user
from ..models import User
from .. import db,photos


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = "Welcome to Scribble"
    title = 'Scribble'
    click_bait = 'In life, you only have 60 seconds to impress someone. 1 minute can make or break you. How do we make sure that you use your 1 minute to actually say something meaningful?'
    return render_template('index.html',  title = title, message = message, click_bait = click_bait)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        return ('not found')
    return render_template('profile.html', user=user)


@main.route('/user/<name>/profile', methods=['POST', 'GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        error = 'The user does not exist'
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('profile/profile.html', form=form)