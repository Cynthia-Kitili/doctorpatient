from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Patient:

    all_patients=[]

    def __init__(self,name,email,category):
        self.name=name
        self.email=email
        self.category

    def save_patient(self):
        Patient.all_patients.append(self) 

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

       


    def __repr__(self):
        return f'User {self.username}'


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))        