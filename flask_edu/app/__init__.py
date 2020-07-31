import os

from flask import Flask
from flask_restful import Resource, Api
from . import config
from flask_cors import *


def create_app(test_config=None):
    print('createxxx app')
    app = Flask(__name__)
    CORS(app,supports_credentials = True)
    app.config.from_object(config)

    from . import db
    db.init_app(app)

    from .api import stack_edu_mqtt
    test = stack_edu_mqtt(app)
    test.send_question('123','{questionId:1}')



    from .api import Quizzes, Admin, QuizResource, jwt
    jwt.init_app(app)
    api = Api(app)
    api.add_resource(Quizzes,'/v1/quizzes')
    api.add_resource(Admin,'/v1/admins')   
    api.add_resource(QuizResource,'/v1/quiz/<int:QuizID>')

    
    return app