from flask import Blueprint, render_template, url_for, flash, session, redirect, g

from forms import LoginForm
from models import User

accounts = Blueprint('accounts', __name__, template_folder='templates', static_folder='static')


@accounts.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            flash('用户名密码错误', 'danger')
        else:
            session['user_id'] = user.id
            flash('欢迎回来', 'success')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

@accounts.route('/logout')
def logout():
    session['user_id'] = None
    g.user = None
    flash('欢迎下次再来', 'success')
    return redirect(url_for('accounts.login'))