# -*- coding：utf-8 -*-
"""
作者:Yutang Lu
日期:2022年06月04日
"""
from SpiderDate import new_total_datalist
from flask import Flask
from sqlalchemy import and_, or_, desc, func
from init import db
from models import Menu
from flask_sqlalchemy import SQLAlchemy
add_flag = 1
delete_flag = 0
delete_date = '2022-06-03'  # 输入要删除的日期
menus = []
count = Menu.query.count()
if count == 0:
    menu_id = count + 1
else:
    max_id = db.session.query(func.max(Menu.id)).first()[0]
    menu_id = max_id + 1


if add_flag:
    for i in new_total_datalist:
        if i[2] == '':
            continue
        menu = Menu(id=menu_id, menu=i[2], canteen=i[1], date=i[0], time=i[3])
        menus.append(menu)
        menu_id += 1
    db.session.add_all(menus)
    db.session.commit()
if delete_flag:
    temp = Menu.query.filter_by(date=delete_date).all()
    for i in temp:
        db.session.delete(i)
        db.session.commit()


