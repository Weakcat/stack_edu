from .db import db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True ,nullable=False)
    type = db.Column(db.String(7), nullable=False)    
    account = db.Column(db.String(8), nullable=False, unique = True)    
    name = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128), nullable = False)
    quizzes = relationship('Quiz', backref='user')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        print(password,self.password_hash)
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'<{self.type} {self.account}>'
    
class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    creat_time = db.Column(db.DateTime, nullable=False)
    creator_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    qas = relationship('QA', backref='quiz')


class QA(db.Model):
    __tablename__ = 'q_a'
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer,nullable=False)
    answer_0 = db.Column(db.String(1),nullable=True)
    answer_1 = db.Column(db.String(6),nullable=True)
    answer_2 = db.Column(db.Integer,nullable=True)
    answer_3 = db.Column(db.String(64),nullable=True)
    quiz_id = db.Column(db.Integer,db.ForeignKey('quiz.id'))
    has_detail = db.Column(db.Integer, nullable=False)

# class Class(db.Model):
#     __tablename__ = 'class'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)


# class Ctrelation(db.Model):
#     __tablename__ = 'ctrelation'
#     id = db.Column(db.Integer, primary_key=True)
#     classid = db.Column(db.Integer)
#     teacherid = db.Column(db.Integer)



# class QADetail(db.Model):
#     __tablename__ = 'q_a_detail'
#     id = db.Column(db.Integer, primary_key=True)
#     q_a_id = db.Column(db.Integer,db.ForeignKey('q_a.id'))
#     question = db.Column(db.String(100),nullable=True)
#     detail = db.Column(db.String(100),nullable=True)

# class QAStudent(db.Model):
#     __tablename__ = 'q_a_student'
#     id = db.Column(db.Integer, primary_key=True)
#     q_a_detail_id   = db.Column(db.Integer, db.ForeignKey('q_a_detail.id'))
#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
