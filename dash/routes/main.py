"""
Default routes
"""
from flask import Blueprint

MAIN_PAGE = Blueprint('main_page', __name__)

@MAIN_PAGE.route('/')
def index():
    """
    At route '/' we are currently only returning "Hello World"
    """
    return "Hello World"
