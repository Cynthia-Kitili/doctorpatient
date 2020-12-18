from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class updateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators = [Required()])
    submit = SubmitField('Submit')

class PatientForm(FlaskForm):
    patient_name = StringField('Patient name:',validators=[Required()])
    patient_category = SelectField('Patient Category:', choices = [('Select category','Select category'),('dermatologist', 'dermatologist'), ('obstetrician', 'obstetrician'),('cardiologist','cardiologist'),('general','general ')], validators=[Required()])
    patient_comment = TextAreaField('Patients Concerns:')
    submit = SubmitField('Submit ')

class DoctorForm(FlaskForm):
    doctor_name = StringField('Name of Doctor:',validators=[Required()])
    doctor_category = SelectField('Field:', choices = [('Select category','Select category'),('dermatologist', 'dermatologist'), ('obstetrician', 'obstetrician'),('cardiologist','cardiologist'),('general','general ')], validators=[Required()])
    doctor_number = StringField('Work Number:',validators=[Required()])
    doctor_hospital=StringField('Hospital:',validators=[Required()])
    submit = SubmitField('Submit ')    

class CommentForm(FlaskForm):
    doc = StringField('Name of Doctor:',validators=[Required()])
    text = TextAreaField('Comment From Doctor:',validators=[Required()])
    book = TextAreaField('Appointment Booking This Week:',validators=[Required()])
    submit = SubmitField('Submit')  
