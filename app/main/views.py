from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from ..models import User,Doctor,Patient,Comment
from .forms import updateProfile,PatientForm,CommentForm,DoctorForm

# views
@main.route('/')
def index():

    """
    view root page function that returns the index page and its data
    """
    title = "Welcome Doctorpatient"
    return render_template('index.html', title = title)
    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        flash('Profile Has Been Updated Successfully!', 'success')

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        flash('Pic Has Been Updated Successfully!', 'success')
    return redirect(url_for('main.profile',uname=uname))

@main.route('/patient/newpatient',methods= ['POST','GET'])
@login_required
def newPatient():
    patient = PatientForm()
    if patient.validate_on_submit():
        name = patient.patient_name.data
        category = patient.patient_category.data
        yourComment = patient.patient_comment.data

        
        newPatient = Patient(patient_name = name,patient_category = category,patient_comment = yourComment,user= current_user)
        db.session.add(newPatient)
        db.session.commit()

        flash('Patient Details Entered Successfully!', 'success')
        #save patient
        newPatient.save_patient()
        return redirect(url_for('.index'))

    title = 'NEW PATIENT'
    return render_template('newPatient.html',title = title,patientform = patient) 

@main.route('/doctor/newdoctor',methods= ['POST','GET'])
@login_required
def newDoctor():
    doctor = DoctorForm()
    if doctor.validate_on_submit():
        name = doctor.doctor_name.data
        number = doctor.doctor_number.data
        hospital = doctor.doctor_hospital.data
        category = doctor.doctor_category.data


        newDoctor = Doctor(doctor_name = name,doctor_category = category,doctor_number=number,doctor_hospital=hospital,user= current_user)
        db.session.add(newDoctor)
        db.session.commit()

        flash('Doctor Details Entered Successfully!', 'success')
        
        #save patient
        newDoctor.save_doctor()
        return redirect(url_for('.index'))

    title = 'NEW DOCTOR'
    return render_template('newDoctor.html',title = title,doctorform = doctor)   

@main.route('/patientcategory/dermatologist',methods= ['POST','GET'])
def displayDermatologistCategory():
    dermatologist = Patient.get_patients('dermatologist')
    return render_template('patientcategory/dermatologist.html',dermatologist = dermatologist)
    
@main.route('/patientcategory/obstetrician',methods= ['POST','GET'])
def displayObstetricianCategory():
    obstetrician = Patient.get_patients('obstetrician')
    return render_template('patientcategory/obstetrician.html',obstetrician = obstetrician)

@main.route('/patientcategory/cardiologist',methods= ['POST','GET'])
def displayCardiologistCategory():
    cardiologist = Patient.get_patients('cardiologist')
    return render_template('patientcategory/cardiologist.html',cardiologist = cardiologist)

@main.route('/patientcategory/general',methods= ['POST','GET'])
def displayGeneralCategory():
    general = Patient.get_patients('general')
    return render_template('patientcategory/general.html',general = general)  

@main.route('/doctorcategory/dermatologist',methods= ['POST','GET'])
def display_DermatologistCategory():
    dermatologist = Doctor.get_doctors('dermatologist')
    return render_template('doctorcategory/dermatologist.html',dermatologist = dermatologist)
    
@main.route('/doctorcategory/obstetrician',methods= ['POST','GET'])
def display_ObstetricianCategory():
    obstetrician = Doctor.get_doctors('obstetrician')
    return render_template('doctorcategory/obstetrician.html',obstetrician = obstetrician)

@main.route('/doctorcategory/cardiologist',methods= ['POST','GET'])
def display_CardiologistCategory():
    cardiologist = Doctor.get_doctors('cardiologist')
    return render_template('doctorcategory/cardiologist.html',cardiologist = cardiologist)

@main.route('/doctorcategory/general',methods= ['POST','GET'])
def display_GeneralCategory():
    general = Doctor.get_doctors('general')
    return render_template('doctorcategory/general.html',general = general)   

@main.route('/comment/<int:id>',methods= ['POST','GET'])
@login_required
def viewPatient(id):
    patient = Patient.getPatientId(id)
    comments = Comment.getComments(id)

    commentForm = CommentForm()
    if commentForm.validate_on_submit():
        comment = commentForm.text.data
        doc = commentForm.doc.data
        book = commentForm.book.data

        newComment = Comment(comment = comment,doc=doc,book=book,user = current_user,patient_id =id)

        newComment.saveComment()

    return render_template('comment.html',commentForm = commentForm,comments = comments,patient = patient)

@main.route('/comment/<int:id>',methods= ['POST','GET'])
@login_required
def viewDoctor(id):
    onedoctor = Doctor.getDoctorId(id)

    return render_template('comment.html',doctor = onedoctor)


@main.route('/about')
def about():
    return render_template('about.html', title = 'About')

