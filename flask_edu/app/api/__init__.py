from flask_expects_json import expects_json

from flask import g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from ..model import User, Quiz, QA
from ..db import db
from .mqttServe import stack_edu_mqtt

#############################################GEVENT部署####################################

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp#md5验证，目前先不整
from flask_restful import Resource, Api

jwt = JWT()

@jwt.authentication_handler
def authenticate(username, password):
    print("login -> ", username, password) 
    user = User.query.filter_by(account = username).first()
    print(user)
    if user.verify_password(password.encode('utf-8')):
        print("User successfully!!!!!!")
        print(user.account)
        return user
    else:
        print('密码错误')

@jwt.identity_handler
def identity(payload):
    print("payload->",payload)
    account = payload['identity']
    print(User.query.get(account))
    return User.query.get(account)


quiz_schema = {
    'type': 'object',
    'properties': {
        'quizNam':{'type': 'string'},
        'QA': {
            'type':'array',
            'items':{
                'orderId': {'type': 'integer'},
                'answer': {'type':'string'}                
            }
        },
        'detailQA': {
            'type':'array',
            'items':{
                'orderId': {'type': 'integer'},
                'question': {'type': 'string'},
                'detail': {'type': 'string'},                
            }
        },
    },
    'required': ['quizNam','QA']
}
#要鉴权jwt，payload里面存储用户信息
class Quizzes(Resource):
    @jwt_required()
    def get(self):
        quizzes = current_identity.quizzes
        quizzes_json = {
            'creator':current_identity.name,
            'quiz':[
                {'id':quiz.id, 'time': quiz.creat_time,'name':quiz.name} for quiz in quizzes
            ]
        }
        return jsonify(quizzes_json)

    # @expects_json(quiz_schema)
    def post(self):
        ...
        return g.data['quizNam']
    def delete(self):
        ...
        return 'delete quiz successfully'

admin_schema = {
    'type': 'object',
    'properties': {
        'type': {'enum': ["Root",'Organ','Teacher','Student']},
        'name': {'type': 'string'},
        'account': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['type','name','account', 'password']
}
class Admin(Resource):
    @jwt_required()
    def get(self):
        print(current_identity.account)
        ...
        return 'get admin'
    @jwt_required()    
    @expects_json(admin_schema)
    def post(self):
        print('regist begin')
        print(current_identity.account)
        print(g.data)
        try:
            users = User(type=g.data['type'], name=g.data['name'], account=g.data['account'], password=g.data['password'])
            db.session.add(users)
            db.session.commit()    
            print('用户注册成功')
            return '用户注册成功'
        except expression:
            print('用户注册失败')
            return '用户注册失败'

class QuizResource(Resource):
    @jwt_required()
    def get(self,QuizID):
        questions = QA.query.filter_by(quiz_id = QuizID).all()
        questions_json = {
            'creator':current_identity.name,
            'question':[
                {'id':question.id, 'order': question.order,'answer':question.answer_0} for question in questions
            ]
        }
        return jsonify(questions_json)