from flask import Flask
from . import models, routes, services

app = Flask(__name__)
routes.init_app(app)

if __name__ == '__main__':
    app.run()
