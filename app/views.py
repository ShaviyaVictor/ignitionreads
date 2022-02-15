from turtle import title
from flask import render_template
from app import app


# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  title = 'Ignition Reads - Landing Page'
  return render_template('index.html', title = title)



@app.route('/reads')
def reads() :
  '''
  View reads page function that returns the reads page
  '''


  return render_template('reads.html')



@app.route('/musings')
def musings() :
  '''
  View musings page function that returns the musings page
  '''

  
  return render_template('musings.html')



@app.route('/gallery')
def gallery() :
  '''
  View gallery page function that returns the gallery page
  '''

  
  return render_template('gallery.html')



@app.route('/about')
def about() :
  '''
  View about page function that returns the about page
  '''

  
  return render_template('about.html')