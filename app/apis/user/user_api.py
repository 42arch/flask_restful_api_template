from flask_restful import Resource, reqparse, abort, fields, marshal

from app.apis.api_constants import USER_ACTION_REGISTER, HTTP_CREATE_SUCCESS, USER_ACTION_LOGIN, HTTP_SUCCESS
from app.ext import cache
from app.models.user_model import User

# 参数解析
parse_base = reqparse.RequestParser()
parse_base.add_argument('password', type=str, required=True, help='please input password')
parse_base.add_argument('action', type=str, required=True, help='please input request argument')

parse_register = parse_base.copy()
parse_register.add_argument('username', type=str, required=True, help='please input username')
parse_register.add_argument('email', type=str, required=True, help='please input email address')

parse_login = parse_base.copy()
parse_login.add_argument('username', type=str, help='please input username')
parse_login.add_argument('email', type=str, help='please input email')

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


class UserResource(Resource):
    def get(self):
        return {'msg': 'get user success'}

    def post(self):
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
                abort(400, msg='user create failed')
            data = {
                'status': HTTP_CREATE_SUCCESS,
                'msg': '用户创建成功',
                'data': user
            }
            return marshal(data, single_user_fields)

        # 用户登录
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
            # token = generate_token()
            token = user.generate_auth_token(expiration=3600)
            # token存入缓存中
            cache.set(token, user.id, timeout=3600)
            data = {
                'status': HTTP_SUCCESS,
                'msg': '用户登录成功',
                'token': token,
                'expiration': 3600
            }
            return data
        else:
            abort(400, msg='please input the correct argument')

