# @Time : 2020/11/15 11:34
# @Author: dan
# @Desc: 初始化项目使用的第三方模块
# @File : extensions.py

from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()
swagger = Swagger()


def init_extensions(app):
    db.init_app(app=app)
    swagger.init_app(app=app)

