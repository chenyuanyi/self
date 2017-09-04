# -*- coding: utf-8 -*-
from flask import session
import time


class SessionTool(object):
    def setNumbersSession(self, dict):
        """
        批量设置session
        :param dict: 
        :return: 
        """
        for key, value in dict.items():
            session[key] = value

    def setExpTime(self, exp_time=7200):
        """
        设置超时时间
        :param exp_time: 
        :return: 
        """
        time_now = time.time()
        exp_date = time_now + exp_time
        session['exp_date'] = exp_date

    def isExpired(self):
        """
        判断session是否过期
        :return: 
        """
        time_now = time.time()
        exp_date = session.get('exp_date', None)
        if exp_date:
            if exp_date < time_now:
                session.clear()
                return {'status': 1, 'message': '登录过期!'}
            else:
                return {'status': 0, 'message': 'ok'}
        else:
            return {'status': -1, 'message': '查无session'}
