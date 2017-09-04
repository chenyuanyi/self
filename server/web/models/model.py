# -*- coding: utf-8 -*-
"""
Created by Chenyuanyi on 2017/9/01
"""
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context

db = SQLAlchemy()

# 将字典格式化方法设置到db.Model基类上

def to_dict(self, filters=()):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns if
                                             c.name not in filters}


db.Model.to_dict = to_dict
db.Model.__str__ = lambda self: str(self.to_dict())
db.Model.__repr__ = lambda self: repr(self.to_dict())


class BusinessDiscount(db.Model):
    __tablename__ = 'business_discount'

    id = db.Column(db.Integer, primary_key=True)
    busi_id = db.Column(db.Integer)
    menu_id = db.Column(db.Integer)
    level = db.Column(db.String(1))
    dis_describe = db.Column(db.String(100))
    dis_begin = db.Column(db.DateTime)
    dis_end = db.Column(db.DateTime)
    dis_way = db.Column(db.String(1))
    dis_compute = db.Column(db.Float)
    dis_price = db.Column(db.Float)
    state = db.Column(db.String(1))
    notice = db.Column(db.String(100))
    is_delete = db.Column(db.String(1))
    create_time = db.Column(db.DateTime)
    create_id = db.Column(db.Integer)
    modify_time = db.Column(db.DateTime)
    modify_id = db.Column(db.Integer)


class BusinessInfo(db.Model):
    __tablename__ = 'business_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type_id = db.Column(db.Integer)
    licence = db.Column(db.String(200))
    place = db.Column(db.String(100))
    try_result = db.Column(db.Text)
    tel1 = db.Column(db.String(20))
    contact1 = db.Column(db.String(20))
    tel2 = db.Column(db.String(20))
    contact2 = db.Column(db.String(20))
    wechat = db.Column(db.String(20))
    qq = db.Column(db.String(20))
    bank_type = db.Column(db.String(30))
    bank_name = db.Column(db.String(20))
    bank_count = db.Column(db.String(50))
    notice = db.Column(db.String(100))
    remark = db.Column(db.Text)
    state = db.Column(db.String(1))
    is_delete = db.Column(db.String(1))
    create_time = db.Column(db.DateTime)
    create_id = db.Column(db.Integer)
    modify_time = db.Column(db.DateTime)
    modify_id = db.Column(db.Integer)


class BusinessType(db.Model):
    __tablename__ = 'business_type'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20))


class EmployeeInfo(db.Model):
    __tablename__ = 'employee_info'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    post = db.Column(db.String(100))
    department = db.Column(db.String(50))
    employ_no = db.Column(db.String(10))
    position = db.Column(db.String(2))
    number = db.Column(db.String(30))
    tel = db.Column(db.String(20))
    qq = db.Column(db.String(20))
    hire_date = db.Column(db.Date)
    fire_date = db.Column(db.Date)
    work_state = db.Column(db.String(1))
    is_delete = db.Column(db.String(1))
    create_time = db.Column(db.DateTime)
    create_id = db.Column(db.Integer)
    modify_time = db.Column(db.DateTime)
    modify_id = db.Column(db.Integer)


class EmployeeOrder(db.Model):
    __tablename__ = 'employee_order'

    id = db.Column(db.Integer, primary_key=True)
    select_id = db.Column(db.Integer)
    busi_menu = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    actual_price = db.Column(db.Float)
    dis_price = db.Column(db.Float)
    balance_way = db.Column(db.String(1))
    state = db.Column(db.String(1))
    is_modify = db.Column(db.String(1))
    is_balance = db.Column(db.String(1))
    notice = db.Column(db.String(100))
    is_delete = db.Column(db.String(1))
    create_time = db.Column(db.DateTime)
    create_id = db.Column(db.Integer)
    modify_time = db.Column(db.DateTime)
    modify_id = db.Column(db.Integer)


class MenuInfo(db.Model):
    __tablename__ = 'menu_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    busi_id = db.Column(db.Integer)
    spec = db.Column(db.String(50))
    photo = db.Column(db.String(50))
    price = db.Column(db.Float)
    state = db.Column(db.String(1))
    notice = db.Column(db.String(100))
    is_delete = db.Column(db.String(1))
    remark = db.Column(db.Text)
    sort = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    create_id = db.Column(db.Integer)
    modify_time = db.Column(db.DateTime)
    modify_id = db.Column(db.Integer)

class SelectDiscount(db.Model):
    __tablename__ = 'select_discount'

    id = db.Column(db.Integer, primary_key=True)
    select_id = db.Column(db.Integer)
    discount_id = db.Column(db.Integer)
    is_delete = db.Column(db.String(1))

class OrderMenu(db.Model):
    __tablename__ = 'order_menu'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    menu_id = db.Column(db.Integer)
    number = db.Column(db.Integer)



class SelectMenu(db.Model):
    __tablename__ = 'select_menu'

    id = db.Column(db.Integer, primary_key=True)
    select_id = db.Column(db.Integer)
    menu_id = db.Column(db.Integer)
    number = db.Column(db.Integer)
    state = db.Column(db.String(1))


class SelectOrder(db.Model):
    __tablename__ = 'select_order'

    id = db.Column(db.Integer, primary_key=True)
    select_date = db.Column(db.Date)
    select_type = db.Column(db.String(1))
    order_state = db.Column(db.String(1))
    order_begin = db.Column(db.DateTime)
    order_end = db.Column(db.DateTime)
    modify_state = db.Column(db.String(1))
    modify_begin = db.Column(db.DateTime)
    modify_end = db.Column(db.DateTime)
    notice = db.Column(db.String(100))
    is_delete = db.Column(db.String(1))
    create_time = db.Column(db.DateTime)
    create_id = db.Column(db.Integer)
    modify_time = db.Column(db.DateTime)
    modify_id = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'user'

    def hash_password(self, password):
        self.passwd = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.passwd)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    passwd = db.Column(db.String(255))
    remark = db.Column(db.String(64))
    permission = db.Column(db.Text)
    is_admin = db.Column(db.String(1))