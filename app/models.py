from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    patients = db.relationship('Patient',backref = 'user',lazy="dynamic")
    doctors = db.relationship('Doctor',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref =  'user',lazy = "dynamic")
    
    @property
    def password(self):

        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    def __repr__(self):
        return f'User {self.username}'


class Patient(db.Model):

    __tablename__ = 'patients'

    id = db.Column(db.Integer,primary_key = True)
    patient_id = db.Column(db.Integer)
    patient_name = db.Column(db.String)
    patient_category = db.Column(db.String)
    patient_comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    comments = db.relationship('Comment',backref =  'patient',lazy = "dynamic")

    def save_patient(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_patients(cls,category):
        patients = Patient.query.filter_by(patient_category=category).all()
        return patients

    @classmethod
    def getPatientId(cls,id):
        patient = Patient.query.filter_by(id=id).first()
        return patient

    @classmethod
    def count_patients(cls,uname):
        user = User.query.filter_by(username=uname).first()
        patients = Patient.query.filter_by(user_id=user.id).all()
        patients_count = 0
        for patient in patients:
            patients_count += 1
        return patients_count

class Doctor(db.Model):

    __tablename__ = 'doctors'

    id = db.Column(db.Integer,primary_key = True)
    doctor_id = db.Column(db.Integer)
    doctor_name = db.Column(db.String)
    doctor_category = db.Column(db.String)
    doctor_hospital = db.Column(db.String)
    doctor_number = db.Column(db.Integer)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_doctor(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_doctors(cls,category):
        doctors = Doctor.query.filter_by(doctor_category=category).all()
        return doctors

    @classmethod
    def getDoctorId(cls,id):
        doctors = Doctor.query.filter_by(id=id).first()
        return doctors

    @classmethod
    def count_doctors(cls,uname):
        user = User.query.filter_by(username=uname).first()
        doctors = Doctor.query.filter_by(user_id=user.id).all()
        doctors_count = 0
        for doctor in doctors:
            doctors_count += 1
        return doctors_count

class Comment(db.Model):
    __tablename__ = 'comments'
 
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(500))
    doc = db.Column(db.String(500))
    book = db.Column(db.String(500))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    patient_id = db.Column(db.Integer,db.ForeignKey("patients.id"))

    def saveComment(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def getComments(cls,patient):
        comments = Comment.query.filter_by(patient_id= patient).all()
        return comments