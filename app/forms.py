import email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField



class RegistrationForm(FlaskForm) :
  '''
  Creating variables to hold our inputs
  '''
  username
  email
  password
  confirm_password
  register