# @Time : 2020/11/15 12:12
# @Author: dan
# @File : manage.py

import os
from flask_migrate import MigrateCommand
from flask_script import Manager
from app import create_app

env = os.environ.get('flask_env') or 'default'
app = create_app(env=env)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
