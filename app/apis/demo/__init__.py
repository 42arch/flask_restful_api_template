# @Time : 2020/11/15 17:52
# @Author: dan
# @File : __init__.py.py

from flask import Blueprint
from flask_restful import Api

from app.apis.demo.demo_api import DemoResource

demo = Blueprint('demo', __name__)
demo_api = Api(demo)

demo_api.add_resource(DemoResource, '/demo/')
