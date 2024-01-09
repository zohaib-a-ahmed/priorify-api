import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    # Secret key for signing cookies, session data, etc.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Supabase configuration
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

