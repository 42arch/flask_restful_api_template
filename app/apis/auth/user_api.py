# @Time : 2020/11/16 22:55
# @Author: dan
# @File : user_api.py
from flask_restful import Resource, reqparse, abort, fields, marshal_with, marshal

from app.extensions import cache
from app.models.user import *

USER_ACTION_LOGIN = 'login'
USER_ACTION_REGISTER = 'register'
HTTP_SUCCESS = 200
HTTP_CREATE_SUCCESS = 201

# 参数解析
parse_base = reqparse.RequestParser()
parse_base.add_argument('password', type=str, required=True, help='please input password')
parse_base.add_argument('action', type=str, required=True, help='please input request argument')

parse_register = parse_base.copy()
parse_register.add_argument('username', type=str, required=True, help='please input username')
parse_register.add_argument('email', type=str, required=True, help='please input email address')

parse_login = parse_base.copy()
parse_login.add_argument('username', type=str, help='please input username')
parse_login.add_argument('email', type=str, help='please input email address')


# 数据对象序列化模板
user_fields = {
    'username': fields.String,
    'password': fields.String(attribute='password_hash'),
    'email': fields.String
}
single_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(user_fields)
}


# 用户数据查询方法
def get_user(user_identity):
    if not user_identity:
        return None
    # 根据id查询
    user = User.query.get(user_identity)
    if user:
        return user
    # 根据邮箱查询
    user = User.query.filter(User.email == user_identity).first()
    if user:
        return user
    # 根据用户名查询
    user = User.query.filter(User.username == user_identity).first()
    if user:
        return user
    return None


class UsersResource(Resource):
    def get(self):
        return "get users"

    def post(self):
        """
        用户注册登录接口
        ---
        parameters:
          - in: path
            name: 用户名
            type: string,
            required: true
          - name: 行为
            in: path
            type: string
            enum: ['register', 'login']
            required: true
          - name: 密码
            in: path
            type: number,
            requierd: true
          - name: 邮箱
            type: string
            required: true
        responses:
          200:
            description: 一个用户信息
            schema:
              id: user

        """
        args = parse_base.parse_args()
        password = args.get('password')
        action = args.get('action').lower()

        # 用户注册
        if action == USER_ACTION_REGISTER:
            args_register = parse_register.parse_args()
            email = args_register.get('email')
            username = args_register.get('username')

            user = User()
            user.username = username
            user.password = password
            user.email = email

            if not user.save():
                abort(400, msg='user created failed')

            data = {
                'status': HTTP_CREATE_SUCCESS,
                'msg': 'user created succeeded',
                'data': user
            }
            return marshal(data, single_user_fields)

        elif action == USER_ACTION_LOGIN:
            args_login = parse_login.parse_args()
            username = args_login.get('username')
            email = args_login.get('email')
            user = get_user(username) or get_user(email)
            if not user:
                abort(400, msg='user does not exist')
            if not user.verify_password(password):
                abort(401, msg='password is not correct')
            if user.is_deleted:
                abort(401, msg='user does not exist')
            token = user.generate_auth_token(exporation=30)
            # token存入缓存中
            print(token)
            cache.set(token, user.id, timeout=30)
            data = {
                'status': HTTP_SUCCESS,
                'msg': '用户登录成功',
                'token': token,
                'expiration': 3600
            }
            return data
        else:
            abort(400, msg='please input the correct argument')