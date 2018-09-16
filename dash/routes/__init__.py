from .main import main_page

def init_app(app):
    app.register_blueprint(main_page)
