# -*- coding: utf-8 -*-
"""
Created by Linjianhui on 2017/3/29
"""
from web import api
from .login import Login
from .menu_tree import MenuTree

api.add_resource(Login, Login.api_url)
api.add_resource(MenuTree, MenuTree.api_url)

from .system import system_router

