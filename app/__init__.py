from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'app/static/img/profile_pics'
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rsrywhxhvptyfs:4YHUoPgsPJQb4hsVEaUwsjEywd@ec2-54-197-249-212.compute-1.amazonaws.com:5432/d7m2kn564j8j0s'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'
app.config['SECRET_KEY'] = 'super secret key'
app.config.from_object('confg')
db = SQLAlchemy(app)


from app import views, models

