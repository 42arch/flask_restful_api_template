# @Time : 2020/11/15 17:51
# @Author: dan
# @File : __init__.py.py
from flask import Blueprint
from flask_restful import Api

from app.apis.auth.logined_test_api import LoginApiResource
from app.apis.auth.user_api import UsersResource

auth = Blueprint("auth", __name__)
auth_api = Api(auth)

auth_api.add_resource(UsersResource, '/users/')
auth_api.add_resource(LoginApiResource, '/logined/')
