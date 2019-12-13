from flask import request, g
from flask_restful import abort

from app.apis.user.model_utils import get_user
from app.ext import cache


def _verify():
    token = request.args.get('token')
    if not token:
        abort(401, msg='not login')

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg='user not available')
    user = get_user(user_id)
    if not user:
        abort(401, msg='user not available')
    g.user = user
    g.auth = token


def login_required(func):
    def wrapper(*args, **kwargs):
        _verify()
        return func(*args, **kwargs)
    return wrapper
