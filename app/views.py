"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, session
from app import db
#from app.models import User
from app.models import Profile_db

import random
import string
import time

from .forms import ProfileForm

###
# Routing for your application.
###

# @app.route('/theform', methods=["GET", "POST"])
# def theform():
#     form = EmailPasswordForm()
#     return render_template('theform.html', form=form)
  
# @app.route('/theform', methods=["GET", "POST"])
# def theform():
#     form = EmailPasswordForm()
#     return render_template('theform.html', form=form)

  
  
@app.route('/')
def index():
    """Render website's home page."""
    return render_template('index2.html')
  
##########################################################################
##########################################################################


# @app.route('/profile', methods=['POST', 'GET'])
# def profile_create():
#   if request.method == 'POST':
#     fname = request.form['fname']
#     lname = request.form['lname']
#     age = request.form['age']
#     sex = request.form['sex']
#     image = request.form['file']
#     userid = random.randint(10000000, 99999999)
#     uname = ''.join([random.choice(fname + lname) for n in xrange(8)]) 
#     prof_add = timeinfo()
#     high_score = 0
#     tdollars = 0
    
#     filename = 'pic.jpg'
#     img = 'img/' + filename
    
#     newusr = Profile.query.filter_by(username = uname).first()
#     if (newusr is None):
#       newprof = Profile(userid, uname, img, fname, lname, sex, age, prof_add, high_score, tdollars)
#       db.session.add(newprof)
#       db.session.commit()
#       flash('new user created')
#     else:
#       flash('user already exist')
#   return render_template('profile2.html')

##########################################################################
##########################################################################
@app.route('/profile', methods=['POST', 'GET'])
def profile_create():
    form = ProfileForm()
    if request.method == 'POST':
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      age = request.form['age']
      sex = request.form['sex']
#      image = request.form['image']
      image = 'pic.jpeg'
      
      userid = random.randint(10000000, 99999999)
      username = ''.join([random.choice(first_name + last_name) for n in xrange(8)]) 
      prof_add = timeinfo()
      high_score = 0
      tdollars = 0
      
      newprofile = Profile_db( userid, username, first_name, last_name, sex, age, prof_add, high_score, tdollars, image)
      db.session.add(newprofile)
      db.session.commit()
      return "{} {} {} {} {} this was a post".format(first_name, last_name, age, sex, image)
    return render_template('newprofile.html', form=form)
  
def timeinfo():
    now = time.strftime("%a, %d %b %Y")
    return now 
  


##########################################################################
########################################################################## 

@app.route('/profiles')
def profiles_list():
    """Render website's home page."""
    return render_template('profiles.html')
  
##########################################################################
########################################################################## 
@app.route('/profiles/<int:id>')
def profile_view(id):
    """Render website's home page."""
    return render_template('user.html')
  
  
##########################################################################
########################################################################## 
@app.route('/person')
def person():
    first_user = db.session.query(Profile_db).first()
    return  " username: {}, prof_add: {}, firstname: {}, lastname: {}, tdollars: {}, image: {}, sex: {}, high_score:{}, age:{}".format(first_user.username,
                                                                                                                                       first_user.prof_add, 
                                                                                                                                      first_user.firstname,
                                                                                                                                       first_user.lastname,
                                                                                                                                       first_user.tdollars, 
                                                                                                                                       first_user.image,
                                                                                                                                       first_user.sex,
                                                                                                                                     first_user.high_score,
                                                                                                                                     first_user.age,)
  
  
  




@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    
    
    app.run(debug=True,host="0.0.0.0",port="8888")
