from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.resources import main
import os

app = Flask(__name__)

# Set the SECRET_KEY
if os.environ.get('SECRET_KEY') is not None:
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
else:
    raise ValueError('SECRET_KEY is not set for the app. Exiting...')
    
# Database setup, initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy()

# Register blueprints
app.register_blueprint(main.main)