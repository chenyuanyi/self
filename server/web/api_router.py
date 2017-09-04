# -*- coding: utf-8 -*-
"""
Created by Linjianhui on 2017/3/29
"""
from flask import session

from web.models.model import User
from . import auth


@auth.verify_password
def verify_password(name, passwd):
    """
    密码认证
    :return:
    """
    is_login = session.get('is_login', False)
    if is_login and name == '':
        return True
    user = User.query.filter(User.name == name).first()
    if user:
        if user.verify_password(passwd):
            session['is_login'] = True
            session['user'] = user.to_dict()
            return True
    return False

from .resources import resources_router
