import random
from datetime import datetime
from threading import Thread
from flask import request, current_app
from flask_mail import Message
from flask_restful import Resource

from app.apis.api_constants import HTTP_SUCCESS
from app.ext import cache, mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, emailcode):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + '账号注册验证码',
                  sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[to])
    msg.body = 'sended by flask-email'
    msg.html = '''
        <h3>
            欢迎来到 <b>Flask_Restful_API_Project</b>!
        </h3>
        <p>
            您的验证码为 &nbsp;&nbsp; <b>{mailcode}</b> &nbsp;&nbsp; 赶快去完善注册信息吧！！！
        </p>
    
        <p>感谢您的支持和理解</p>
        <p>来自：Flask_Restful_API_Project</p>
        <p>{time}</p>
    '''.format(mailcode=emailcode, time=datetime.utcnow)
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return thread


class SendEmailCodeResource(Resource):
    def post(self):
        email = request.form.get('email')
        if email is None:
            return {'msg': '请填写邮箱地址'}

        email_code = '%06d' % random.randint(0, 99999)
        # cache.set('EmailCode:' + email, email_code, 1800)

        send_mail(to=email, emailcode=email_code)
        return {
            'status': HTTP_SUCCESS,
            'msg': '验证码发送成功',
            'code': email_code
        }