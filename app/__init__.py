from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




# Initializing our app
app = Flask(__name__)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)


# Setting up the configuration
app.config.from_object(DevConfig)

app.config['SECRET_KEY']='shashaviya'

# db configuration for SQLAlchemy sqlite
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/reads.db'


# db configuration for SQLAlchemy postgresql 
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Access@localhost/ignition'




from app import views