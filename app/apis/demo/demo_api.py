# @Time : 2020/11/15 17:53
# @Author: dan
# @File : demo_api.py
import os

from flask import current_app
from flask_restful import Resource


class DemoResource(Resource):
    def get(self):
        app = current_app._get_current_object()

        MAIL_SERVER = os.getenv('MAIL_SERVER')
        MAIL_PORT = os.getenv("MAIL_PORT")

        return {'server': MAIL_SERVER, 'port': MAIL_PORT}
