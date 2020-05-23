import os

from flask import Flask, current_app, g, request, \
    session, make_response, render_template, redirect, abort, render_template_string, url_for, flash

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

import constants
from forms import UserForm, UserAvatarForm

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.secret_key='abcdefg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost:9002/test_falsk'
app.config['WTF_SCRF_SECRET_KEY'] = 'abcdefg123456'
app.config['UPLOAD_PATH'] = os.path.join(os.path.dirname(__file__), 'medias')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__= 'weibo_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0)


class UserAddress(db.Model):
    __tablename__= 'weibo_user_address'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('weibo_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))

@app.before_request
def before_request():
    g.user = 'zhangsan'


@app.context_processor
def inject_const():
    return dict({
        'constants': constants
    })


@app.route('/')
def index():
    print(url_for('index', _external=True))
    print(url_for('mine', _external=True))
    return render_template('index.html')
    # print(current_app)
    # return 'index'
    # html = """
    # <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <title>Title</title>
    #     </head>
    #     <body>
    #     ddddddd
    #     </body>
    #     </html>
    # """
    # return render_template_string(html)


@app.route('/m')
def mine():
    return render_template('mine.html')


@app.route('/var')
def var():
    user_dict = {
        'username': 'zhangsan',
        'address.city': '广州',
        'address.town': '镇'
    }
    list_city = [
        '北京',
        '上海',
        '广州'
    ]
    list_obj = [
        {'user': 'zhangsan'},
        {'user': 'wangwu'}
    ]
    return render_template('var.html', user_dict=user_dict, list_city=list_city, list_obj=list_obj)


@app.route('/tag')
def use_tag():
    var = None
    list_obj = {
        'user1': 'zhangsan',
        'user2': 'wangwu',
        'user3': 'lisi'
    }
    hello = 'hello locy'
    html = '<h5>hello world</h5>'
    phone = '15980256438'

    flash('欢迎回来')
    return render_template('tag.html', var=var, list_obj=list_obj,
                           hello=hello, html=html, phone=phone)


@app.template_filter('phone_format')
def phone_format(phone_no):
    return phone_no[0:3]+'***'


@app.route('/test')
def test():
    flash('成功', 'success')
    flash('失败', 'error')
    return redirect('/msg')


@app.route('/msg')
def msg():
    return render_template('msg.html')


@app.route('/user/add', methods=['post', 'get'])
def add_user():
    # form = UserForm(csrf_enabled=False)
    form = UserForm()
    # print(form.is_submitted())
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        birth_date = form.birth_date.data
        age = form.age.data
        user = User(username=username, password=password, birth_date=birth_date, age=age)
        # print(username, user)
        db.session.add(user)
        db.session.commit()
    else:
        print(form.errors)
    return render_template('add_user.html', form=form)


@app.route('/img/upload', methods=['post', 'get'])
def img_upload():
    base_dir = app.config['UPLOAD_PATH']
    form = UserAvatarForm()
    if form.validate_on_submit():
        f = form.avatar.data
        filename = secure_filename(f.filename)
        file_name = os.path.join(base_dir, filename)
        f.save(file_name)
    else:
        print(form.errors)

    return render_template('img_upload.html')


    # base_dir = app.config['UPLOAD_PATH']
    # print(base_dir)
    # if request.method == 'POST':
    #     files = request.files
    #     file1 = files['file1']
    #     file2 = files['file2']
    #     print(files)
    #     print(file1)
    #     if file1:
    #         filename = secure_filename(file1.filename)
    #         file_name = os.path.join(base_dir, filename)
    #         print(file_name)
    #         file1.save(file_name)
    # return render_template('img_upload.html')


if __name__ == '__main__':
    app.run()
