# -*- coding：utf-8 -*-
"""
作者:Yutang Lu
日期:2022年06月04日
"""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:111111@localhost/menu_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # 避免警告
db = SQLAlchemy(app)
