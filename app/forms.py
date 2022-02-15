import email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email



class RegistrationForm(FlaskForm) :
  '''
  Creating variables to hold our inputs
  '''
  username = StringField(label = 'Username', validators=[DataRequired(), Length(min=3, max=15)] )
  email = StringField(label = 'Email', validators=[DataRequired(), Email()])
  password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6, max=16)])
  confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])

  submit = SubmitField(label='REGISTER')



class LoginForm(FlaskForm) :
  '''
  Creating variables to hold our inputs for the Login form
  '''
  email = StringField(label = 'Email', validators=[DataRequired(), Email()])
  password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6, max=16)])

  submit = SubmitField(label='LOGIN')