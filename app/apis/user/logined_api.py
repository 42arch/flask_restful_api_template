from flask import g
from flask_restful import Resource

from app.apis.user.utils import login_required


# 传入token，登录验证后才能获取的内容
class LoginApiResource(Resource):
    @login_required
    def get(self):
        user = g.user
        print(user.username)
        return {
            'msg': 'post ok',
            'logined_user': user.username
        }
