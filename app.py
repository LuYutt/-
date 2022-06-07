# -*- coding：utf-8 -*-
"""
作者:Yutang Lu
日期:2022年06月04日
"""
from flask import render_template, request
from sqlalchemy.orm import context
from init import db
from init import app
from models import Menu


@app.route('/')
def index():
    # UserAgent = request.headers.get('user-agent')
    # return f'hello!{UserAgent}'
    # 类
    temp = db.session.query(Menu).filter(Menu.id>=1).all()
    canteen = []
    date = []
    for dish in temp:
        if dish.canteen not in canteen:
            canteen.append(dish.canteen)
        if dish.date not in date:
            date.append(dish.date)
    return render_template('index.html', canteen=canteen, date=date)


@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        canteen = request.form.get("canteen")
        date = request.form.get("date")
        menus = db.session.query(Menu).filter(Menu.date==date, Menu.canteen==canteen).all()
    return render_template('ChooseShow.html', menus=menus)


if __name__ == '__main__':
    app.run(debug=True)

