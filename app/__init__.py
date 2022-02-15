from flask import Flask
from .config import DevConfig




# Initializing our app
app = Flask(__name__)



# Setting up the configuration
app.config.from_object(DevConfig)
app.config['SECRET_KEY']='shashaviya'


from app import views