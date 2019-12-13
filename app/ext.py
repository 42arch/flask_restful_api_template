from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
sess = Session()
mail = Mail()
cache = Cache(config={
    "CACHE_TYPE": "redis"
})
cors = CORS()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    sess.init_app(app)
    # 邮件支持
    mail.init_app(app)
    # 缓存
    cache.init_app(app)
    # 跨域
    cors.init_app(app)
