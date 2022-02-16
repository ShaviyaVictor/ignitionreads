from crypt import methods
from flask import render_template, url_for, redirect
from app import app
from app.forms import RegistrationForm, LoginForm


# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''


  title = 'Home~Landing Page'
  return render_template('index.html', title = title)




@app.route('/reads')
def reads() :
  '''
  View reads page function that returns the reads page
  '''


  title = 'Reads~Just4Reads'
  return render_template('reads.html', title = title)



@app.route('/musings')
def musings() :
  '''
  View musings page function that returns the musings page
  '''

  
  title = 'Musings~All reflections'
  return render_template('musings.html', title = title)



@app.route('/gallery')
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

  
  title = 'Login'
  form = LoginForm()

  if form.validate_on_submit():
    
    if form.email.data=='shaviyavictor@gmail.com' and form.password.data=='12345678' :
      return redirect(url_for('reads'))

    else :
      return redirect(url_for('index'))

  return render_template('login.html', title = title, form = form)



@app.route('/signup', methods=['POST', 'GET'])
def signup() :
  '''
  View signup page function that returns the signup page
  '''

  
  title = 'Register'
  form = RegistrationForm()

  if form.validate_on_submit():
    return redirect(url_for('login'))

  return render_template('signup.html', title = title, form = form)