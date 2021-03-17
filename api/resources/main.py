from flask.blueprints import Blueprint
from flask import request

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return 'Hello, World', 200

@main.route('/whoami')
def whoami():
    return f"Hi, you have tried to access this site from {request.headers.get('HOST')} via {request.headers.get('USER-AGENT')}"