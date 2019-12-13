from flask import Blueprint
from flask_restful import Api

from app.apis.user.logined_api import LoginApiResource
from app.apis.user.send_email_code import SendEmailCodeResource
from app.apis.user.user_api import UserResource

user = Blueprint('user', __name__)
user_api = Api(user)

user_api.add_resource(UserResource, '/user/')
user_api.add_resource(LoginApiResource, '/logined/')
user_api.add_resource(SendEmailCodeResource, '/sendemailcode/')
