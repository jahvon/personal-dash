from flask import Blueprint

main_page = Blueprint('main_page', __name__)

@main_page.route('/')
def index():
    return "Hello World"
