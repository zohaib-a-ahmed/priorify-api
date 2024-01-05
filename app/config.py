import os

class Config(object):
    # Secret key for signing cookies, session data, etc.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-hard-to-guess-string'

    # Database configuration
    # Adjust the URI based on your database type and credentials
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///yourapp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Set to False to disable a Flask-SQLAlchemy feature that requires extra memory

    # Supabase configuration
    SUPABASE_URL = os.environ.get('db.mbsdesbuxkhlsmbcahvw.supabase.co')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

    # Other configurations can be added here
