# -*- coding：utf-8 -*-
"""
作者:Yutang Lu
日期:2022年06月04日
"""
from init import db


class Menu(db.Model):
    __tablename__ = 'Menu'
    id = db.Column(db.Integer, primary_key=True)
    menu = db.Column(db.String(50), nullable=True)
    canteen = db.Column(db.String(50), nullable=True)
    date = db.Column(db.Date, nullable=True)
