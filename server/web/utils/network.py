# -*- coding: utf-8 -*-
import base64

from config import ISBASE64

try:
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass

import json

import binascii
import requests
import hashlib

try:
    from urllib import urlencode, quote
except ImportError:
    from urllib.parse import urlencode, quote


def user_center_http(param):
    """
    用户中心http请求
    :param param:
    :return:
    """
    url = param['url']
    data = 'd=' + quote(urlencode(param['data']))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    try:
        r = requests.post(url, data=data, headers=headers, timeout=30)
        res = r.text
        res = json.loads(res)
        res['Info'] = '提交成功' if res['Stat'] == 0 else ('提交失败' if res['Info'] == '' else res['Info'])
    except requests.exceptions.ConnectionError:
        res = {"Info": "ConnectionError", "Stat": 10001, "ActionId": 0}
    except requests.exceptions.Timeout:
        res = {"Info": "Timeout", "Stat": 10001, "ActionId": 0}
    except ValueError:
        res = {"Info": "No JSON", "Stat": 10001, "ActionId": 0}
    except binascii.Error:
        res = {"Info": "base64解码异常", "Stat": 10001, "ActionId": 0}
    return res


def game_server_http_single(param, res_list=None):
    """
    单个游戏服务端http请求
    :param param:
    :param res_list:
    :return:
    """
    server_id = param.get('server_id', None)
    url = param['url']
    data = param['data']
    if server_id and isinstance(server_id, str):
        server_arr = server_id.split('_')
        data['serverid'] = int(server_arr[1])
        data['appid'] = int(server_arr[0])
    encode_data = 'd=' + quote(urlencode(data))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    try:
        r = requests.post(url, data=encode_data, headers=headers, timeout=30)
        res = r.text
        if ISBASE64 == 1:
            res = base64.decodestring(res)
        res = json.loads(res)
        res['Info'] = '提交成功' if res['Stat'] == 0 else ('提交失败' if res['Info'] == '' else res['Info'])
    except requests.exceptions.ConnectionError:
        res = {"Info": "ConnectionError", "Stat": 10001, "ActionId": 0}
    except requests.exceptions.Timeout:
        res = {"Info": "Timeout", "Stat": 10001, "ActionId": 0}
    except ValueError:
        res = {"Info": "No JSON", "Stat": 10001, "ActionId": 0}
    except binascii.Error:
        res = {"Info": "base64解码异常", "Stat": 10001, "ActionId": 0}
    res['server_id'] = server_id
    if res_list is None:
        return res
    else:
        res_list.append(res)


if __name__ == '__main__':
    data = {
        'ActionId': 31020,
        'appid': 1010,
        'serverid': 1
    }
    param = {
        'url': 'http://192.168.7.21:30003/frontend',
        'server_id': '',
        'data': data
    }
    net_res = game_server_http_single(param)

    # 注册测试
    # account = 'dq2admin'
    #
    # m = hashlib.md5()
    # m.update('123456')
    # pwd = m.hexdigest()
    # l = len(pwd) / 2
    # pwd_list = [pwd[x:x + l] for x in [0, l]]
    # s = pwd_list[0] + account + pwd_list[1]
    # m = hashlib.md5()
    # m.update(s)
    # password = m.hexdigest()
    #
    # register_param = {
    #     'url': 'http://192.168.7.21:60003/frontend',
    #     'data': {
    #         'RetailId': 9,
    #         'Status': 1,
    #         'Account': account,
    #         'Password': password,
    #         'DeviceId': 'dq_home2',
    #         'DeviceType': 'pc',
    #         'DeviceOs': 'windows 7',
    #         'GameId': 102,
    #         'ActionId': 1101
    #     }
    # }
    #
    # register_res = user_center_http(register_param)
    print(net_res)
