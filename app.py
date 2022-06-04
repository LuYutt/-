# -*- coding：utf-8 -*-
"""
作者:Yutang Lu
日期:2022年06月04日
"""
from flask import render_template

from init import app


@app.route('/')
def index():
    # UserAgent = request.headers.get('user-agent')
    # return f'hello!{UserAgent}'
    # 类
    class Person(object):
        name = u'luyutang'
        age = 20
    I = Person()
    context = {
        'username': u'luyutang',
        'gender': u'男',
        'age': 22,
        'person': I,  # 声明
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **context)


@app.route('/user/<name>')
def hello(name):
    return f'hello {name}!!'


if __name__ == '__main__':
    app.run(debug=True)

