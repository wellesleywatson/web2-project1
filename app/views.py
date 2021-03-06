"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, jsonify, send_from_directory
from werkzeug import secure_filename
from app.models import Profile_db
from .forms import ProfileForm
from flask import Response

import random
import string
import time
import json
import os


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


#####################################################################################################################################  
#####################################################################################################################################
  
@app.route('/')
def index():
    """Render website's home page."""
    return render_template('index2.html')
  
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
      userid = random.randint(10000000, 99999999)
      username = ''.join([random.choice(first_name + last_name) for n in xrange(8)]) 
      prof_add = timeinfo()
      high_score = 0
      tdollars = 0
      
      image = request.files['image']
      if image and allowed_file(image.filename):
        filename = str(userid) + '_' + secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
      
      newprofile = Profile_db( userid, username, first_name, last_name, sex, age, prof_add, high_score, tdollars, filename)
      db.session.add(newprofile)
      db.session.commit()
      getuser = Profile_db.query.filter_by(username=username).first()
      reply = "User: {} {}  now has a profile. Please see profile below."
      msg = reply.format(first_name, last_name)
      return redirect('/profiles')
    return render_template('newprofile.html', form=form)
  
def timeinfo():
    now = time.strftime("%a, %d %b %Y")
    return now 

  
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
  

        
      


##########################################################################
########################################################################## 
@app.route('/profiles',methods=['POST', 'GET'])
def profiles_list():
    profiles = Profile_db.query.all()
    storage = []
    if request.method == 'POST':
      for users in profiles:
        storage.append({'userid':users.userid, 'username':users.username, 'firstname':users.firstname, 'lastname':users.lastname, 'sex':users.sex, 'age':users.age, 'prof_add':str(users.prof_add), 'high_score':users.high_score, 'tdollars':users.tdollars, 'image':users.image})
      users = {'users': storage}
      return json.dumps(users)
    else:
      return render_template('profiles.html',profiles=profiles)
  
##########################################################################
########################################################################## 
@app.route('/profiles/<int:id>',methods=['POST', 'GET'])
def profile_view(id):
    profile = Profile_db.query.get(id)
    load_pic = reload_file(profile)
    date = profile.prof_add
    val = date.strftime("%a, %d %b %Y")
    if request.method == 'POST':
      return jsonify(age=profile.age, 
                     username=profile.username, 
                     #firstname=profile.firstname, 
                     #lastname=profile.lastname, 
                     sex=profile.sex,
                     userid=profile.userid,
                     prof_add=str(val), 
                     high_score=profile.high_score, 
                     tdollars=profile.tdollars, 
                     image=profile.image)
    else:
      return render_template('user.html',profile=profile,time=val, load_pic=load_pic )
    
    
def reload_file(filename):
    return url_for('static', filename='img/profile_pics/'+filename.image)
  
 
##########################################################################
########################################################################## 
@app.route('/person')
def person():
    val = db.session.query(Profile_db).all()
    first_user = val[1]
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
