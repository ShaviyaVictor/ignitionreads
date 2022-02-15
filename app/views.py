from flask import render_template
from app import app


# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''


  return render_template('index.html')



@app.route('/reads')
def reads() :
  '''
  View reads page function that returns the reads page
  '''

  return render_template('reads.html')