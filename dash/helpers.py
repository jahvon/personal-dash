from requests_oauthlib import OAuth2Session
from dash import app

# Google Auth Helper
class Google:
    @staticmethod
    def get_google_auth(state=None, token=None):
        if token:
            return OAuth2Session(app.config['CLIENT_ID'], token=token)
        if state:
            return OAuth2Session(app.config['CLIENT_ID'], state=state, redirect_uri=app.config['REDIRECT_URI'])
        oauth = OAuth2Session(app.config['CLIENT_ID'], redirect_uri=app.config['REDIRECT_URI'], scope=app.config['SCOPE'])
        return oauth

    @staticmethod
    def get_google_auth_url():
        google = Google.get_google_auth()
        return google.authorization_url(app.config['AUTH_URI'], access_type='offline')

    @staticmethod
    def get_google_auth_token(state, request):
        google = Google.get_google_auth(state=state)
        return google.fetch_token(app.config['TOKEN_URI'], client_secret=app.config['CLIENT_SECRET'], authorization_response=request)

    @staticmethod
    def get_google_user_info(token):
        google = Google.get_google_auth(token=token)
        return google.get(app.config['USER_INFO'])