from flask import Flask, current_app, g, request, \
    session, make_response, render_template, redirect, abort, render_template_string, url_for, flash

import constants

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.secret_key='abcdefg'


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


if __name__ == '__main__':
    app.run()
