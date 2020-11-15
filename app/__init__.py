# @Time : 2020/11/15 10:43
# @Author: dan
# @File : __init__.py.py

from flask import Flask

from app.apis import register_blueprint
from config import envs


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    register_blueprint(app)

    return app

