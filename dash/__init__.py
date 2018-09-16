from flask import Flask
from . import models, routes, services

APP = Flask(__name__)
routes.init_app(APP)

if __name__ == '__main__':
    APP.run()
