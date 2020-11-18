# @Time : 2020/11/15 11:34
# @Author: dan
# @Desc: 初始化项目使用的第三方模块
# @File : extensions.py
from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_session import Session
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
session = Session()
cache = Cache()

template = {
  "swagger": "2.0",
  "info": {
    "title": "Flask Restful Api",
    "description": "基于Flask构建的Restful api应用",
    "contact": {
      "responsibleOrganization": "ME",
      "responsibleDeveloper": "Me",
      "email": "me@me.com",
      "url": "www.me.com",
    },
    "termsOfService": "http://me.com/terms",
    "version": "0.1.1"
  },
  "host": "localhost:5000",  # overrides localhost:500
  # "basePath": "/api",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}

swagger = Swagger(template=template)


def init_extensions(app):
    # ORM支持
    db.init_app(app=app)
    # 数据库迁移
    # migrate.init_app(app=app, db=db)
    migrate.init_app(app=app, db=db, render_as_batch=True)  # 数据库为sqlite时
    # 邮件支持
    mail.init_app(app=app)
    # 会话
    session.init_app(app=app)
    # 缓存
    cache.init_app(app=app, config={'CACHE_TYPE': 'redis'})
    # swagger文档支持
    swagger.init_app(app=app)

