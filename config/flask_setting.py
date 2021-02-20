class Config:
    # flask配置文件
    DEBUG = True

    # Flask-SQLAlchemy配置文件
    # mysql+pymysql://用户名:密码@host:端口/database名
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sparrow_UI:sparrow123@127.0.0.1:3306/myflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 屏蔽警告
    SQLALCHEMY_ECHO = True  # 调试用


class DevelopmentConfig(Config):
    # flask配置文件
    ENV = 'development'


class ProductionConfig(Config):
    # flask配置文件
    ENV = 'production'
    DEBUG = False
