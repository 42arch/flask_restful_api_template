# @Time : 2020/11/15 13:24
# @Author: dan
# @Desc: hello_world程序
# @File : __init__.py.py
from app.apis.auth import auth
from app.apis.demo import demo
from app.apis.index import index


# 路由蓝图注册
def register_blueprint(app):
    app.register_blueprint(index)
    app.register_blueprint(demo)
    app.register_blueprint(auth)

