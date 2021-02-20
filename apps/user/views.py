import hashlib

from flask import Blueprint, request, render_template, url_for
from sqlalchemy import or_, and_
from werkzeug.utils import redirect

from apps.user.instance import User_value
from apps.user.model import User
from ext import db

user_bp = Blueprint('user', __name__)


# users = []  # 保存用户对象

@user_bp.route('/', endpoint='index')
def user_center():
    """

    :return: response
    """
    # 查询数据库所有user数据
    users = User.query.filter(User.isdelete == False).order_by(User.rdatetime).all()  # select * from user;
    # print(users)  # [user_objectA, user_objectB, ...]

    return render_template('user/center.html', users=users)
    # return render_template('user/show.html', users=users)


@user_bp.route('/delete', endpoint='del')
def delete_user():
    # # 获取show.html传递过来的username
    # username = request.args.get('username')
    # # 根据username找到列表users里的内容并删掉
    # for user in users:
    #     if user.username == username:
    #         # 删除user对象
    #         users.remove(user)
    #         return redirect('/')
    # return render_template('user/show.html', msg='删除失败')

    # 利用ORM方式获取数据
    id = request.args.get('id')
    # 获取id对应用户
    user = User.query.get(id)
    # 判断该ID是否存在，存在则删除
    if user:
        # 逻辑删除该客户，物理上不删除
        user.isdelete = True
        # 物理删除该客户
        # db.session.delete(user)
        # 提交该操作
        db.session.commit()
        return redirect('/')

    return render_template('user/center.html', msg='该数据不存在，删除失败！')


@user_bp.route('/update', methods=['GET', 'POST'], endpoint='upd')
def update_user():
    # 获取update.html传递过来的参数
    if request.method == 'POST':
        id = request.form.get('id')
        print('进入update的post请求')
        print('id: ', id)
        # 获取id对应用户
        user = User.query.get(id)
        print('user: ', user)
        if user:
            user.username = request.form.get('username')
            user.password = hashlib.sha256(request.form.get('password').encode('utf-8')).hexdigest()
            user.phone = request.form.get('phone')
            db.session.commit()
            return redirect('/')

        return render_template('user/center.html', msg='无此客户，修改失败！')

    else:
        print('进入update的get请求')
        id = request.args.get('id')
        # 根据id定位到update.html页面
        user = User.query.get(id)
        if user:
            return render_template('user/update.html', user=user)

        return render_template('user/center.html', msg='客户信息不存在，请重新选择！')


@user_bp.route('/search')
def search():
    print('跳转到search页面')
    search = request.args.get('search')

    if search:
        print('search: ', search)
        users = User.query.filter(
            and_(User.isdelete == False, or_(User.username.contains(search), User.phone.contains(search)))).order_by(
            User.rdatetime).all()
        return render_template('user/center.html', users=users)
    else:
        return redirect(url_for('user.index'))


#
# @user_bp.route('/search_username', methods=['POST'], endpoint='search_username')
# def search_user():
#     print('跳转到search_name页面')
#     username = request.form.get('search_name')
#
#     if username:
#         print('username: ', username)
#         users = User.query.filter(User.username.contains(username)).all()
#
#     return render_template('user/center.html', users=users)
#
#
# @user_bp.route('/search_phone')
# def search_phone():
#     print('跳转到search_phone页面')
#     phone = request.args.get('search_phone')
#
#     if phone:
#         print('phone: ', phone)
#         users = User.query.filter(User.phone.contains(phone)).all()
#     print('users: ', users)
#
#     return render_template('user/center.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')
def register_blueprint():
    """

    :return: response
    """
    if request.method == 'POST':
        # 将前端页面的数据传回后台
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        # 判断如果两次密码一致，则创建User对象
        if password == repassword:
            # 使用model持久化的方式存储数据
            user_db = User()
            user = user_db.query.filter_by(username=username).all()
            # 判断用户名唯一性
            if user:
                return render_template('user/register.html', msg='用户名已存在！')

            user_db.username = username
            user_db.password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # 密码加密
            user_db.phone = phone

            # 将一条数据添加入数据库中，session相当于缓存
            db.session.add(user_db)
            db.session.commit()

            # # 使用列表的方式存储数据
            # user = User_value(username, password, phone)
            # # 将user对象加入users列表中
            # users.append(user)
            # print(url_for('user.index'))  # 反响解析
            return redirect(url_for('user.index'))
        else:
            return render_template('user/register.html', msg='两次密码不一致！')

    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def login_blueprint():
    """

    :return: response
    """
    if request.method == 'POST':
        # 将前端页面的数据传回后台
        username = request.form.get('username')
        password = hashlib.sha256(request.form.get('password').encode('utf-8')).hexdigest()

        # 查询数据库所有user数据
        users = User.query.all()  # select * from user;
        # 判断登录账户和密码与数据库是否一致
        for user in users:
            if user.username == username:
                if user.password != password:
                    return render_template('user/login.html', msg='账号密码不一致，请重新输入！')
                else:
                    return redirect(url_for('user.index'))
        return render_template('user/login.html', msg='没有该账户，请重新输入！')
    else:
        return render_template('user/login.html')


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout_blueprint():
    """

    :return: response
    """
    return '客户退出'
