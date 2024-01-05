from flask import Blueprint

# Create a Blueprint for your views
views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def hello_world():
    return "Hello, World!"
