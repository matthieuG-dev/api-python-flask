#! /usr/bin/python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import uuid
from werkzeug.security import generate_password_hash, \
    check_password_hash
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Init app
app = Flask(__name__)

app.config.from_pyfile('config.py')

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# IMPORT MODELS
from models import *

db.create_all()

from views import *

if __name__ == '__main__':
    app.run(debug=True)