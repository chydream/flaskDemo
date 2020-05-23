import uuid
from functools import wraps

from flask import Flask, current_app, g, request, \
    session, make_response, render_template, redirect, abort, render_template_string, url_for, flash

from accounts.views import accounts
from mall.views import mall
from forms import LoginForm, UserForm, ProductEditForm, LoginFormNew
from models import db, User

app = Flask(__name__)
app.secret_key='abcdefg'
app.config.from_object('conf.Config')
#使用orm
db.init_app(app)
#注册蓝图
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(mall, url_prefix='/mall')


@app.before_request
def before_request():
    user_id = session.get('user_id', None)
    if user_id:
        user = User.query.get(user_id)
        g.user = user


@app.route('/')
def index():
    print(app.url_map)
    return render_template('index.html')


@app.route('/form')
def page_form():
    form = LoginFormNew()
    return render_template('form.html', form=form)


def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id', None)
        if not user_id:
            flash('请登录', 'danger')
            return redirect(url_for('login'))
        return view_func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    app.run()
