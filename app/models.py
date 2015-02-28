from . import db

class Profile_db(db.Model):
    userid = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    sex = db.Column(db.String(6))
    age = db.Column(db.Integer)
    prof_add = db.Column(db.Date)
    high_score = db.Column(db.Integer)
    tdollars = db.Column(db.Integer)
    image = db.Column(db.String(80))
    
    
    
    
    
    
    def __init__(self, userid, username, firstname, lastname, sex, age, prof_add, high_score, tdollars, image):
        self.userid = userid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age
        self.prof_add = prof_add
        self.high_score = high_score
        self.tdollars = tdollars
        self.image = image

    def __repr__(self):
        return '<Profile %r %r>' % (self.firstname, self.lastname)