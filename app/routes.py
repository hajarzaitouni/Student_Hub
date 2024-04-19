from flask import abort, render_template, redirect, url_for, request, flash, session
from app import app, bcrypt
from app.forms import LoginAdminForm
from app.models import Admin, Student, Class, Subject, Result, SubjectMarks
from app import db




#============================**** Admin Area ****==================================


@app.route("/admin/")
@app.route("/admin/login", methods=['GET', 'POST'])
def adminLogin():
    # Create an instance of the LoginAdminForm
    form = LoginAdminForm()  
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == '' or password == '':
            flash('Please enter a correct email/password !', 'danger')
            return redirect('adminLogin')
        
        admin = Admin.query.filter_by(email=email).first()
        if admin and bcrypt.check_password_hash(admin.password, password):
            session['loggedin'] = True
            session['admin_id'] = admin.id
            session['admin_email'] = admin.email
            flash('Login successful', 'success')
            return redirect('dashboard')
        else:
            flash('Invalid Email or Password', 'danger')
    return render_template('management/admin_login.html', title='Login', form=form)


#admin dashboard
@app.route("/admin/dashboard")
def dashboard():
    if 'loggedin' in session and 'admin_id' in session:
        admin_id = session['admin_id']
        admin = Admin.query.get(admin_id)
        if admin:
            return render_template('management/dashboard.html', title='Dashboard', authenticated=True)
    
    # If the user is not authenticated or admin_id is not in session, redirect to admin login
    return redirect(url_for('adminLogin'))

#logout from admin dashboard
@app.route('/admin/logout')
def adminLogout():
    if 'loggedin' in session:
        # Clear the session data
        session.clear()
        # Redirect to the admin login page
        return redirect(url_for('adminLogin'))
    # If the admin is not logged in, redirect to the admin login page
    return redirect(url_for('adminLogin'))

#---------------------------- STUDENTS ------------------------------#

@app.route('/admin/student', methods = ['GET', 'POST'])
def student():
    if 'loggedin' in session:      
        students = Student.query.all()
        classes = Class.query.all()
        return render_template("management/student.html",
                               title='Student Management', students=students, classes=classes)
    return redirect(url_for('adminLogin'))

@app.route("/admin/edit_student", methods=['GET'])
def edit_student():
    if 'loggedin' in session:      
        student_id = request.args.get('student_id')
        student = Student.query.get(student_id)
        classes = Class.query.all()
        return render_template("management/edit_student.html",
                               title='Student Management', student=student, classes=classes)
    return redirect(url_for('adminLogin'))


@app.route("/admin/save_student", methods=['POST'])
def save_student():
    if 'loggedin' in session:
        print("Form Data:", request.form)
        if request.method == 'POST' and 'admission_no' in request.form:
            admission_no = request.form['admission_no']
            roll_no = request.form['roll_no']  
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            academic_year = request.form['academic_year']
            admission_date = request.form['admission_date']
            gender = request.form['gender']
            date_of_birth = request.form['date_of_birth']
            father_name = request.form['father_name']
            mother_name = request.form['mother_name']
            address = request.form['address']
            mobile = request.form['mobile']
            father_occup = request.form['father_occupation']
            mother_occup = request.form['mother_occupation']
            
            action = request.form['action']
            
            
            if action == 'updateStudent':
                student_id = request.form['student_id']
                student = Student.query.get(student_id)
                student.admission_no = admission_no
                student.roll_no = roll_no
                student.first_name = first_name
                student.last_name = last_name
                student.email = email
                student.academic_year = academic_year
                student.admission_date = admission_date
                student.gender = gender
                student.date_of_birth = date_of_birth
                student.father_name = father_name
                student.mother_name = mother_name
                student.address = address
                student.mobile = mobile
                student.mother_occupation = mother_occup
                student.father_occupation = father_occup
            else:
                class_id = request.form['class_id']
                student = Student(admission_no=admission_no, roll_no=roll_no,
                                  first_name=first_name, last_name=last_name, email=email,
                                  class_id=class_id, academic_year=academic_year, admission_date=admission_date,
                                  gender=gender, date_of_birth=date_of_birth, father_name=father_name,
                                  mother_name=mother_name, father_occupation=father_occup)
                db.session.add(student)
            
            db.session.commit()
            flash('Student saved successfully!', 'success')
            return redirect(url_for('student'))
        flash('Error occurred while saving student!', 'danger')
        return redirect(url_for('student'))
    else:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('adminLogin'))

@app.route("/admin/delete_student", methods=['GET'])
def delete_student():
    if 'loggedin' in session:    
        student_id = request.args.get('student_id')
        student = Student.query.get(student_id)
        if student:
            db.session.delete(student)
            db.session.commit()
            flash('Student deleted successfully!', 'success')
        else:
            flash('Student not found!', 'danger')
        return redirect(url_for('student'))
    return redirect(url_for('adminLogin'))


  #---------------------------- CLASSES ------------------------------#

@app.route("/admin/classes", methods =['GET', 'POST'])
def classes():
    if 'loggedin' in session:
        classes = Class.query.all()
        return render_template('management/class.html',
                               title='Class Management', classes=classes)
    return redirect(url_for('adminLogin'))

@app.route("/admin/save_class", methods=['POST'])
def save_class():
    if 'loggedin' in session:
        if request.method == 'POST' and 'level' in request.form:
            class_id = request.form['classid']
            level = request.form['level']
            section = request.form['section']
            action = request.form['action']

            if action == 'updateClass':
                class_obj = Class.query.get(class_id)
                class_obj.level = level
                class_obj.section = section
            else:
                new_class = Class(level=level, section=section)
                db.session.add(new_class)

            db.session.commit()
            return redirect(url_for('classes'))
        else:
            flash('Please fill out the form field!', 'danger')
        return redirect(url_for('classes'))
    return redirect(url_for('adminLogin'))

@app.route("/admin/edit_class", methods=['GET'])
def edit_class():
    if 'loggedin' in session:
        class_id = request.args.get('class_id')
        class_obj = Class.query.get(class_id)
        if class_obj:
            return render_template("management/edit_class.html",
                                   title='Class Management', class_obj=class_obj)
        else:
            flash('Class not found!', 'danger')
            return redirect(url_for('classes'))
    return redirect(url_for('adminLogin'))

@app.route("/admin/delete_class", methods =['GET'])
def delete_class():
    if 'loggedin' in session:    
        class_id = request.args.get('class_id')
        class_obj = Class.query.get(class_id)
        if class_obj:
            db.session.delete(class_obj)
            db.session.commit()
            flash('Class deleted successfully!', 'success')
        else:
            flash('Class not found!', 'danger')
        return redirect(url_for('classes'))
    return redirect(url_for('adminLogin'))

  #---------------------------- SUBJECT ------------------------------#

@app.route("/admin/subject", methods =['GET', 'POST'])
def subject():
    if 'loggedin' in session:
        subjects = Subject.query.all()
        classes = Class.query.all()
        return render_template('management/subject.html',
                               title='Subject List', subjects=subjects, classes=classes)
    return redirect(url_for('adminLogin'))


@app.route("/admin/save_subject", methods=['POST'])
def save_subject():
    if 'loggedin' in session:
        if request.method == 'POST' and 'subject_name' in request.form:
            subject_name = request.form['subject_name']
            action = request.form['action']
            
            if action == 'updateSubject':
                subject_id = request.form['subject_id']
                subject = Subject.query.get(subject_id)
                subject.subject_name = subject_name
            else:
                new_subject = Subject(subject_name=subject_name)
                db.session.add(new_subject)

            db.session.commit()
            return redirect(url_for('subject'))
        else:
            flash('Please fill out the form field!', 'danger')
        return redirect(url_for('subject'))
    return redirect(url_for('adminLogin'))

@app.route("/admin/edit_subject", methods =['GET'])
def edit_subject():
    if 'loggedin' in session:
        subject_id = request.args.get('subject_id') 
        subject = Subject.query.get(subject_id)
        return render_template("management/edit_subject.html",
                               title='Subject List', subject=subject)
    return redirect(url_for('adminLogin'))    


@app.route("/delete_subject", methods =['GET'])
def delete_subject():
    if 'loggedin' in session:
        subject_id = request.args.get('subject_id') 
        subject = Subject.query.get(subject_id)
        db.session.delete(subject)
        db.session.commit()  
        return redirect(url_for('subject'))
    return redirect(url_for('adminLogin'))

                
 #---------------------------- RESULT ------------------------------#  

@app.route("/admin/result", methods =['GET', 'POST'])
def result():
    if 'loggedin' in session:
        results = Result.query.all()
        students = Student.query.all()
        subjects = Subject.query.all()            
        return render_template('management/result.html',
                               title='Result Management', results=results,
                               students=students, subjects=subjects)
    return redirect(url_for('adminLogin'))


@app.route("/admin/edit_result/<int:result_id>", methods=['GET', 'POST'])
def edit_result(result_id):
    if 'loggedin' in session:
        result = Result.query.get_or_404(result_id)
        if request.method == 'POST':
            # Retrieve form data
            student_id = request.form['student_id']
            semester = request.form['semester']
            #subject_id = request.form['subject']
            subject_marks_marks = request.form.getlist('subject_marks_marks')
            subject_marks_subjects = request.form.getlist('subject_marks_subjects')
            subject_marks_marks = [int(mark) for mark in subject_marks_marks]
            subject_marks_subjects = [int(subject) for subject in subject_marks_subjects]

            # Update result attributes
            result.student_id = student_id
            result.semester = semester

            # Delete existing subject marks associated with this result
            SubjectMarks.query.filter_by(result_id=result.id).delete()

            # Add updated subject marks
            for mark, subject in zip(subject_marks_marks, subject_marks_subjects):
                new_subject_marks = SubjectMarks(result=result, subject_id=subject, marks=mark)
                db.session.add(new_subject_marks)

            # Commit changes to the database
            db.session.commit()

            flash('Result updated successfully!', 'success')
            return redirect(url_for('result'))
        else:
            # Render edit result template with necessary data
            students = Student.query.all()
            subjects = Subject.query.all()
            return render_template('management/edit_result.html', result=result, students=students, subjects=subjects)
    else:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('adminLogin'))


@app.route("/admin/save_result", methods=['POST'])
def save_result():
    if 'loggedin' in session:
        if request.method == 'POST' and 'student_id' in request.form:
            student_id = request.form['student_id']
            semester = request.form['semester']
            subject_id = request.form['subject']
            subject_marks_marks = request.form.getlist('subject_marks_marks')
            subject_marks_subjects = request.form.getlist('subject_marks_subjects')
            subject_marks_marks = [int(mark) for mark in subject_marks_marks]
            subject_marks_subjects = [int(subject) for subject in subject_marks_subjects]
            action = request.form['action']

            if action == 'updateResult':
                result_id = request.form['result_id']
                result = Result.query.get(result_id)
                if result:
                    result.student_id = student_id
                    result.semester = semester
            else:
                student = Student.query.get(student_id)
                subject = Subject.query.get(subject_id)
                new_result = Result(student=student, semester=semester)
                db.session.add(new_result)
                db.session.commit()
                
                for mark, subject in zip(subject_marks_marks, subject_marks_subjects):
                    new_subject_marks = SubjectMarks(result=new_result, subject_id=subject, marks=mark)
                    db.session.add(new_subject_marks)
                    db.session.commit()
            flash('Result saved successfully!', 'success')
            return redirect(url_for('result'))
        else:
            flash('Error occurred while saving result!', 'danger')
            return redirect(url_for('result'))
    else:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('adminLogin'))

@app.route("/admin/delete_result/<int:result_id>", methods=['POST', 'GET'])
def delete_result(result_id):
    if 'loggedin' in session:
        result = Result.query.get(result_id)
        if result:
            # Delete associated subject marks
            subject_marks = SubjectMarks.query.filter_by(result_id=result_id).all()
            for mark in subject_marks:
                db.session.delete(mark)

            # Delete the result
            db.session.delete(result)
            db.session.commit()
            flash('Result deleted successfully!', 'success')
        else:
            flash('Result not found!', 'danger')
        return redirect(url_for('result'))
    else:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('adminLogin'))




#-----------------User Area------------------------

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'roll_number' in request.form:
        roll_number = request.form['roll_number']
        student = Student.query.filter_by(roll_no=roll_number).first()
        if roll_number and student:
            session['user_logged_in'] = True
            session['roll_number'] = roll_number
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid roll number. Please try again.', 'error')
    
    return render_template('public/login.html')


@app.route("/dashboard", methods=['GET'])
def home():
    if 'user_logged_in' in session:
        roll_number = session['roll_number']
        student = Student.query.filter_by(roll_no=roll_number).first()
        if student is None:
            abort(404)
        return render_template('public/home.html', student=student)

    return render_template('public/login.html')


@app.route("/subjects", methods=['GET'])
def subjects():
    if 'user_logged_in' in session:
        roll_number = session['roll_number']
        student = Student.query.filter_by(roll_no=roll_number).first()
        if student:
            return redirect(url_for('record', student_id=student.id))
        
    return render_template('public/login.html')


@app.route("/record/student/<int:student_id>", methods=['GET'])
def record(student_id):
    if 'user_logged_in' in session:
        student = Student.query.get_or_404(student_id)
        if student:
            return render_template('public/record.html', student=student)
        
    return render_template('public/login.html')


@app.route("/view/result/<int:student_id>/<string:semester>/", methods=['GET'])
def view_result(student_id, semester):
    if 'user_logged_in' in session:
        student = Student.query.get_or_404(student_id)
        if student:
            # Retrieve results for the student
            student_results = Result.query.filter_by(student_id=student_id, semester=semester).all()
            # Iterate through each result and fetch associated subject marks
            for result in student_results:
                result.subject_marks = SubjectMarks.query.filter_by(result_id=result.id).all()
            return render_template('public/view_result.html', student=student, results=student_results)
        
    return render_template('public/login.html')

@app.route("/profile", methods=['GET'])
def profile():
    if 'user_logged_in' in session:
        if 'user_logged_in' in session and 'roll_number' in session:
            roll_number = session['roll_number']
            # Query the database to get the student with the provided roll number
            student = Student.query.filter_by(roll_no=roll_number).first()
            if student:
                # Render the student profile template with student data
                return render_template('public/profile.html', student=student)
    
    return redirect(url_for('login'))
     
        
@app.route('/logout')   
def logout():
    if 'user_logged_in' in session:
        # Clear the session data
        session.clear()
        # Redirect to the login page
        return redirect(url_for('login'))
    # If the user is not logged in, redirect to the login page
    return redirect(url_for('login'))




