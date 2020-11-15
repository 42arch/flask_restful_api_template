# @Time : 2020/11/15 13:53
# @Author: dan
# @File : index.py

from flask import request, Blueprint, jsonify

index = Blueprint('index', __name__)


@index.route('/', methods=['GET'])
def get_index():
    return "<h1>Flask服务启动成功<h1>"

