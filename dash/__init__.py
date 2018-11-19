import os
from flask import Flask
from flask_login import LoginManager
from OpenSSL import SSL

app = Flask(__name__, static_folder="./static")
app.config.from_object(os.environ['APP_SETTINGS'])

# Routes
from dash.routes import base, auth
app.register_blueprint(base)
app.register_blueprint(auth, url_prefix="/auth")

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

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('./key.pem')
context.use_certificate_file('./cert.pem')

if __name__ == '__main__':
    app.run(ssl_context=context)
