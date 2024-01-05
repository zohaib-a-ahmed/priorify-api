from flask import Flask
# from flask_cors import CORS
from .config import Config

# Initialize the Flask application
app = Flask(__name__)

# Apply configurations from the config.py file
app.config.from_object(Config)

# Enable CORS if needed for your frontend
# CORS(app)

# Import and register blueprints/routes
from .views import views_bp
app.register_blueprint(views_bp)

# Import and initialize database components if needed
# from .models import db
# db.init_app(app)

# You might also want to initialize Flask-Migrate here

# This allows you to run the app with `flask run` from the terminal
if __name__ == '__main__':
    app.run(debug=True)
