# -*- coding: utf-8 -*-
"""
Created by Linjianhui on 2017/1/18
用户管理
"""
import json

from flask_restful import Resource
from flask import request, session

from web import auth, app
from meun_config import menu_config
from web.models.model import User, db
from . import api_path


class UserManage(Resource):
    decorators = [auth.login_required]
    api_url = [api_path + 'user_manage', api_path + 'user_manage/<int:user_id>', api_path + 'user_manage/<flag>']

    def get(self, **kwargs):
        """

        :return:
        """
        if 'user_id' in kwargs:
            user_id = kwargs['user_id']
            user_permission = self.get_menu_data_by_user(user_id)
            if user_permission:
                if user_permission.permission:
                    return json.loads(user_permission.permission)
                else:
                    return {}
            else:
                return {'status': 400, 'msg': '用户不存在'}
        else:
            if len(kwargs) != 0:
                return {
                    'menu_data': self.get_all_menu_data()
                }
            else:
                return self.get_all_user_data()

    def get_all_user_data(self):
        """
        获取所有用户
        :return:
        """
        user_list = db.session.query(User.id, User.name, User.remark).all()
        data = [{'id': item.id, 'name': item.name, 'remark': item.remark} for item in
                user_list]
        return data

    def get_all_menu_data(self):
        """
        获取所有导航菜单数据
        :return: 
        """
        menu_data = menu_config
        return menu_data

    def get_menu_data_by_user(self, user_id):
        """
        获取某个用户的导航菜单数据权限
        :param user_id: 
        :return: 
        """
        menu_permission = db.session.query(User.permission).filter(User.id == user_id).first()
        return menu_permission

    def post(self):
        """
        post
        :return:
        """
        flag_fun_dict = {
            'change_password': self.change_password,
            'create_user': self.create_user,
            'delete_user': self.delete_user,
            'save_permission': self.save_permission
        }
        form_data = request.get_json()
        flag = form_data['flag']
        fun = flag_fun_dict.get(flag)
        if fun:
            return fun(form_data)
        else:
            return {'state': 405, 'msg': '未知操作'}

    def change_password(self, form_data):
        """
        修改密码
        :param form_data:
        :return:
        """
        user_id = form_data['user_id']
        new_password = form_data['new_password']
        user = User.query.filter(User.id == user_id).first()
        user.hash_password(new_password)
        db.session.commit()
        return {'state': 0, 'msg': '密码修改成功'}

    def create_user(self, form_data):
        """
        创建用户
        :param form_data:
        :return:
        """
        new_user = User(
            name=form_data['name'],
            remark=form_data['remark']
        )
        new_user.hash_password(form_data['password'])

        db.session.add(new_user)
        db.session.commit()
        res = {'state': 0, 'msg': '用户创建成功'} if new_user.id else {'state': 1, 'msg': '用户创建失败'}
        return res

    def delete_user(self, form_data):
        """
        删除用户
        :param form_data:
        :return:
        """
        user_id = form_data['user_id']
        if user_id == session['user']['id']:
            return {'state': 1, 'msg': '请不要删除自己!'}
        if User.query.count() > 1:
            User.query.filter(User.id == user_id).delete()
            db.session.commit()
            res = {'state': 0, 'msg': '删除用户成功'}
        else:
            res = {'state': 1, 'msg': '至少保留一个用户'}
        return res

    def save_permission(self, form_data):
        """
        保存权限
        :param form_data: 
        :return: 
        """
        permission = form_data['permission']
        permission_str = json.dumps(permission, separators=(',', ':'))
        uesr_id = form_data['user_id']
        User.query.filter(User.id == uesr_id).update({
            User.permission: permission_str
        })
        db.session.commit()
        return {'state': 0, 'msg': '权限修改成功'}
