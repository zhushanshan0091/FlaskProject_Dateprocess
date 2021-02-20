# -*- coding: utf-8 -*-
from flask import Flask

from apps.user.view import user_bp
from config.flask_setting import DevelopmentConfig
from ext import db, bootstrap


def creat_app():
    # app是一个核心对象，重新定义template和static文件夹位置
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)  # 增加配置

    # 初始化db，将db对象与app进行关联
    db.init_app(app)

    # 初始化bootstrap
    bootstrap.init_app(app=app)

    # 注册蓝图
    app.register_blueprint(user_bp)  # 将蓝图对象绑定到app上
    # print(app.url_map)

    return app
