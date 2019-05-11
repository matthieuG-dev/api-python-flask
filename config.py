
from app import basedir

DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/api.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEYS = False

SECRET_KEY = 'secretkey'