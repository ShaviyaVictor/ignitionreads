# from crypt import methods
import email
from flask import render_template, url_for, redirect, flash
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User
import requests
import json
from flask_login import login_user, logout_user,  current_user, login_required


# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''


  title = 'Home~Landing Page'
  return render_template('index.html', title = title)




@app.route('/reads', methods=['GET'])
@login_required
def reads() :
  '''
  View reads page function that returns the reads page
  '''


  title = 'Reads~Just4Reads'

  req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
  # obj = json.loads(req.content)
  # listed = list(obj.items())
  # data = listed

  data = json.loads(req.content)

  # json_data = json.loads(data)


  return render_template('reads.html', title = title, data = data)



@app.route('/musings')
@login_required
def musings() :
  '''
  View musings page function that returns the musings page
  '''

  
  title = 'Musings~All reflections'
  return render_template('musings.html', title = title)



@app.route('/gallery')
@login_required
def gallery() :
  '''
  View gallery page function that returns the gallery page
  '''

  
  title = 'Gallery~Memory photo dump'
  return render_template('gallery.html', title = title)



@app.route('/about')
def about() :
  '''
  View about page function that returns the about page
  '''

  
  title = 'About~Ignition Reads'
  return render_template('about.html', title = title)


@app.route('/login', methods=['POST', 'GET'])
def login() :
  '''
  View login page function that returns the login page
  '''

  if current_user.is_authenticated :
    return redirect(url_for('index'))
  
  title = 'Login'
  form = LoginForm()

  if form.validate_on_submit():

    user = User.query.filter_by(email=form.email.data).first()
    
    if user and bcrypt.check_password_hash(user.password, form.password.data) :

      login_user(user)

      flash(f'Logged in successful as {form.email.data}', category='success')

      return redirect(url_for('reads'))

    else :
      flash(f'Login unsuccessful for {form.email.data}', category='danger')

  return render_template('login.html', title = title, form = form)


@app.route('/logout')
def logout() :
  logout_user()

  return redirect(url_for('login'))



@app.route('/signup', methods=['POST', 'GET'])
def signup() :
  '''
  View signup page function that returns the signup page
  '''

  if current_user.is_authenticated :
    return redirect(url_for('index'))
  
  
  title = 'Register'
  form = RegistrationForm()

  if form.validate_on_submit():

    #password hashing
    encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

    user = User(username=form.username.data, email=form.email.data, password=encrypted_password)
    db.session.add(user)
    db.session.commit()

    flash(f'Account created successful for {form.username.data}', category='success')

    return redirect(url_for('login'))

  return render_template('signup.html', title = title, form = form)