# -*- coding: utf-8 -*-

from web import api
from .user_manage import UserManage

api.add_resource(UserManage, *UserManage.api_url)
