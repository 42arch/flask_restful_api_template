import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


# 通用配置类
class Config:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'RANDOWSECRETLEYSSSS8S73F'

    # 日志 配置

    # session 设置
    SESSION_TYPE = 'redis'
    SESSION_COOKIE_SECURE = True
    SESSION_USE_SIGNER = True

    # 邮件配置
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 25
    MAIL_USERNAME = "xxx@163.com"
    MAIL_PASSWORD = "password"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_SUBJECT_PREFIX = '[Flask_API]'


# 开发环境(sqllite数据库)
class DevelopmentConfig(Config):
    DEBUG = True
    # dbinfo = {
    #     "ENGINE": "postgresql",
    #     "DRIVER": "psycopg2",
    #     "USER": "postgres",
    #     "PASSWORD": "123",
    #     "HOST": "localhost",
    #     "PORT": '5432',
    #     "NAME": "testdb"
    # }
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'example.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



# 测试环境(postgresql数据库)
class TestConfig(Config):
    TESTING = True
    dbinfo = {
        "ENGINE": "postgresql",
        "DRIVER": "psycopg2",
        "USER": "postgres",
        "PASSWORD": "123",
        "HOST": "localhost",
        "PORT": '5432',
        "NAME": "testdb"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


# 生产环境（mysql数据库）
class ProductionConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "Home410793!",
        "HOST": "localhost",
        "PORT": '3306',
        "NAME": "FlaskProductDb"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopmentConfig,
    "testing": TestConfig,
    "product": ProductionConfig,
    "default": DevelopmentConfig
}