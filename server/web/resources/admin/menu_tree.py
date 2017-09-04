# -*- coding: utf-8 -*-
"""
Created by Linjianhui on 2017/3/29
"""
from copy import deepcopy

import json
from flask import session
from flask_restful import Resource
from meun_config import menu_config
from web import auth

from . import api_path


class MenuTree(Resource):
    decorators = [auth.login_required]
    api_url = api_path + 'menu'

    def get(self):
        menu_data = menu_config
        user = session['user']
        if user:
            if user['permission']:
                menu_permission = json.loads(user['permission']).get('menu')
            else:
                menu_permission = []
            return self.menu_filter(menu_data, menu_permission)
        else:
            return {'state': 401, 'msg': '用户未登录'}
        # return menu_data

    def menu_filter(self, menu_data, menu_permission):
        """
        递归去除导航
        :param menu_data:
        :param menu_permission:
        :return:
        """
        new_menu_data = []
        for menu_item in menu_data:
            if menu_item['index'] in menu_permission:
                new_menu_data.append(menu_item)
            elif 'children' in menu_item:
                new_children = self.menu_filter(menu_item['children'], menu_permission)
                if len(new_children) > 0:
                    new_item = deepcopy(menu_item)
                    new_item['children'] = new_children
                    new_menu_data.append(new_item)
        return new_menu_data
