# -*- coding: utf-8 -*-
"""
Created by Linjianhui on 2017/1/9
"""
import os

from flask import session
from flask_restful import Resource
from web import auth
from . import api_path


class Login(Resource):
    decorators = [auth.login_required]
    api_url = api_path + 'login'

    def post(self):
        user_name = session['user']['name']
        return {'status': 'ok', 'user_name': user_name}

    def get(self):
        """
        用户退出
        :return:
        """
        session['user'] = None
        session['is_login'] = False
        tmp_file = session.get('tmp_file')
        if tmp_file:
            try:
                os.remove(tmp_file)
            except:
                pass
        return {'status': 'ok'}
