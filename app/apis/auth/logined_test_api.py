# @Time : 2020/11/18 23:38
# @Author: dan
# @File : logined_test_api.py
from flask import g
from flask_restful import Resource

from app.apis.auth.common import login_required


class LoginApiResource(Resource):
    @login_required
    def get(self):
        user = g.user
        print(user)
        return {
            'msg': 'get logined api successful',
            'logined_user': user.username
        }
