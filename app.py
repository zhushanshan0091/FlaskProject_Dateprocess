from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.model import User, UserInfo

from apps import creat_app
# 初始化flask对象

from ext import db

app = creat_app()
# 使用命令操作
manager = Manager(app=app)
# 命令工具，与app建立联系
migrate = Migrate(app=app, db=db)
# 给manager增加一个自定义命令，操作数据库   建立migrate与manager之间的联系
# 将migrate对数据库的操作命令加入manager中，通过manager操作app
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    print('初始化****************')


if __name__ == '__main__':
    manager.run()  # port=5000
    # 没有使用manager的时候用以下方式
    # app.run(port=5093)
