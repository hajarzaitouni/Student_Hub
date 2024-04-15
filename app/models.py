from app import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    admission_no = db.Column(db.String(100), unique=True, nullable=False)
    roll_no = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    academic_year = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False, default='Male')
    photo = db.Column(db.String(100), nullable=False, default='default.jpg')
    admission_date = db.Column(db.String(100), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False, default='Marrakech')
    mobile = db.Column(db.String(15), nullable=False, default='3333333333')
    father_occupation = db.Column(db.String(100), nullable=False)
    mother_occupation = db.Column(db.String(100), nullable=False, default='House Wife')
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    
    class_rel = db.relationship('Class', backref=db.backref('students', lazy=True))

    
    def __repr__(self):
        return f"<Student'{self.admission_no}', '{self.first_name} {self.last_name}'>"

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(100), nullable=False)
    section = db.Column(db.String(100), nullable=False)
    
    
    
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(100), nullable=False)
    
    subject_marks = db.relationship("SubjectMarks", back_populates="subject")

    
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    semester = db.Column(db.String(100), nullable=False)
    
    student = db.relationship('Student', backref=db.backref('results', lazy=True))
    subject_marks = db.relationship("SubjectMarks", back_populates="result")

    def __repr__(self):
        return f"<Result {self.student_id} - {self.semester}>"
    
    @property
    def CountSubjects(self):
        return len(self.subject_marks)
    
    @property
    def average(self):
        if not self.subject_marks:
            return 0
        total_score = sum(score_result.marks for score_result in self.subject_marks)
        average = total_score / len(self.subject_marks)
        return round(average, 2)

class SubjectMarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result_id = db.Column(db.Integer, db.ForeignKey('result.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    marks = db.Column(db.Float, nullable=False, default=0)
    
    result = db.relationship('Result', back_populates='subject_marks')
    subject = db.relationship('Subject', back_populates='subject_marks')

    def __repr__(self):
        return f"<SubjectMarks {self.result_id} - {self.subject_id}>"