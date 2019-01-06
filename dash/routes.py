import json

from requests.exceptions import HTTPError

from dash.forms import LoginForm
from dash.helpers import Google, Env
from dash.models import User, db
from flask import (Blueprint, Response, abort, redirect, render_template,
                   request, session, url_for, flash)
from flask_login import current_user, login_required, login_user, logout_user
from jinja2 import TemplateNotFound

base = Blueprint('base', __name__, template_folder='templates')
auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base.index'))
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        check_user = User.query.filter_by(username=username).first()
        if check_user is not None and check_user.check_password(password):
            check_user.login()
            db.session.commit()
            login_user(check_user)
            return redirect(url_for('base.index'))
        else:
            flash('Invalid username or password')
    
    if Env.is_development:
        return render_template('pages/login.html', dev=True)
    else:
        auth_url, state = Google.get_google_auth_url()
        session['oauth_state'] = state
        return render_template('pages/login.html', auth_url=auth_url)

@auth.route('/gCallback')
def callback():
    # Redirect user to home page if already logged in.
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('base.index'))
    if 'error' in request.args:
        if request.args.get('error') == 'access_denied':
            return 'You denied access.'
        return 'Error encountered.'
    if 'code' not in request.args and 'state' not in request.args:
        return redirect(url_for('login'))
    else:
        # Execution reaches here when user has successfully authenticated our app.
        try:
            token = Google.get_google_auth_token(state=session['oauth_state'], request=request.url)
        except HTTPError:
            return 'HTTPError occurred.'
        resp = Google.get_google_user_info(token=token)
        if resp.status_code == 200:
            user_data = resp.json()
            email = user_data['email']
            user = User.query.filter_by(email=email).first()
            # Create account if it does not exist
            if user is None:
                user = User()
                user.email = email
            # Update attributes with data pulled from Google
            user.name = user_data['name']
            user.tokens = json.dumps(token)
            user.avatar = user_data['picture']
            db.session.add(user)
            # Update the user's last login time
            updated_user = user.login()
            db.session.commit()
            # Login User
            login_user(updated_user)
            flash('You were successfully logged in')
            return redirect(url_for('base.index'))
        return 'Could not fetch your information.'

@base.route('/')
@login_required
def index():
    return render_template('pages/index.html')


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You were successfully logged out.')
    return redirect(url_for('auth.login'))

@base.errorhandler(401)
def unauthorized(e):
    return redirect(url_for('auth.login'))

@base.errorhandler(404)
def page_not_found(e):
    return Response('<p>Page not found</p>')
