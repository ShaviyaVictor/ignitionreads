from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy




# Initializing our app
app = Flask(__name__)




# Setting up the configuration
app.config.from_object(DevConfig)

app.config['SECRET_KEY']='shashaviya'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/reads.db'


from app import views