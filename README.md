# flask项目模板

## 目录结构

```txt
app                主应用文件夹
    - __init__.py  应用创建
    - apis         视图层文件夹
    - models       数据层(ORM模型文件夹)        
    - ext.py       第三方插件文件
migrations         数据库迁移文件夹
config.py          配置文件
manage.py          项目入口文件
requirements.txt   项目依赖
```

## 使用

* cd到目录下执行`pip install -r requirements.txt`安装依赖；

* 在config.py文件内修改数据库配置，里面有四个环境配置，选一即可，然后在manage.py文件`app = create_app('develop')`导入相应配置；

* 数据库迁移
  在Models/models.py 里已创建了一个ORM对象（测试）Student，执行以下命令进行数据迁移，并应用到数据库。结果会在配置的数据库中生成一个student表，包含name和age两个列。

  >`python manage.py db init`
  >`python manage.py db migrate -m 'init migration'`
  >`python manage.py db upgrade`

* 运行`python manage.py runserver`命令，开启服务；

## api
* 用户注册:  [POST] http://127.0.0.1:5000/api/user/?action=register
* 用户登录： [POST] http://127.0.0.1:5000/api/user/?action=login
* 登录验证：  [GET] http://127.0.0.1:5000/api/logined/?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
* 发送邮箱验证码:：[POST] http://127.0.0.1:5000/api/sendemailcode/