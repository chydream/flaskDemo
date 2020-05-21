from flask import Flask, current_app, g, request, \
    session, make_response, render_template, redirect, abort, render_template_string

app = Flask(__name__)

@app.before_first_request
def first_request():
    print('first')


@app.before_request
def before_request():
    print('before')

@app.after_request
def after_request(resp):
    print('after')
    return resp


@app.teardown_request
def teardown_request(resp):
    print('teardown')
    return resp


@app.route('/')
def hello_world():
    page = request.args.get('page', None)
    print(page)
    name = request.values.get('name', None)
    print(name)
    headers = request.headers
    host = headers.get('host', None)
    print(headers)
    print(host)
    ip = request.remote_addr
    print(ip)
    return 'Hello World!'


@app.route('/hello/<username>')
def hello(username):
    return '你好' + username


@app.route('/page')
@app.route('/page/<page>')
def list_user(page=None):
    return '当前页：{}'.format(page)


def index():
    # print(current_app)
    # return 'index'
    # return render_template('index.html')
    html = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        
        </body>
        </html>
    """
    return render_template_string(html)

app.add_url_rule('/index', 'index', index)
print(app.url_map)


@app.route('/test')
def test():
    # return ('找不到了', 404, {
    #     'user_id': 'abc123'
    # })
    # resp = make_response(
    #     '这是一个测试', 404
    # )
    # resp.headers['token'] = 'my token'
    # return resp

    print('业务逻辑')
    ip_list = ['127.0.0.1']
    ip = '127.0.0.1'
    if ip in ip_list:
        abort(403)
    return redirect('/html')


@app.errorhandler(404)
def not_found(err):
    print(err)
    return '您要的页面丢失了'


@app.route('/html')
def html():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
