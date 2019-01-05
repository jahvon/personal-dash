import os
from flask import Flask
from flask_login import LoginManager
from flask_scss import Scss

app = Flask(__name__, static_folder="./static")
app.config.from_object(os.environ['APP_SETTINGS'])

# Routes
from dash.routes import base, auth
app.register_blueprint(base)
app.register_blueprint(auth, url_prefix="/auth")

# Assets
Scss(app, static_dir='dash/static', asset_dir='dash/assets')

# Database and models
from dash.models import User

# Authorization
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    app.run()
