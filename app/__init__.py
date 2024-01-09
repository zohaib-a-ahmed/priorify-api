from flask import Flask
from flask_cors import CORS
from .config import Config
from supabase import create_client, Client

app = Flask(__name__)
app.config.from_object(Config)
supabase: Client = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

from .views import views_bp
app.register_blueprint(views_bp)

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
