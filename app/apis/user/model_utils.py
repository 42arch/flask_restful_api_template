# 用户数据查询方法
from app.models.user_model import User


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
