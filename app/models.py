import email

from click import password_option
from app import db




class User(db.Model) :
  id
  username
  email
  image_file
  password
  date_created