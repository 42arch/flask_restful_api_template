# @Time : 2020/11/18 23:28
# @Author: dan
# @File : common.py
from flask import request, g
from flask_restful import abort

from app.extensions import cache
from app.models.user import User


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


def _verify():
    # token = "ss"
    # token = request.args.get('token')
    token = request.headers.get('token')
    if not token:
        abort(401, msg='you are not login')

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg="user not available")
    user = get_user(user_id)
    if not user:
        abort(401, msg="user not available")
    g.user = user
    g.auth = token


def login_required(func):
    def wrapper(*args, **kwargs):
        _verify()
        return func(*args, **kwargs)
    return wrapper
