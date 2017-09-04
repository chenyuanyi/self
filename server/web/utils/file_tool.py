# -*- coding: utf-8 -*-
import os
import time

from flask import session, json
from werkzeug.utils import secure_filename


def save_file(file_obj, upload_path, *params):
    """
    :param file_obj: 文件
    :param upload_path: 保存路径
    :return: 
    """
    file_type = params[0] if params else ''
    if file_type:
        tmp_file = session.get(file_type)
    else:
        tmp_file = session.get('tmp_file')
    if tmp_file:
        try:
            os.remove(tmp_file)
        except:
            pass
    image_name = '%d-%s' % (int(time.time()), secure_filename(file_obj.filename))
    save_path = os.path.join(upload_path, image_name)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    file_obj.save(save_path)
    if file_type:
        session[file_type] = save_path
        list_file = session.get('list_file') if session.get('list_file') else {}
        list_file[file_type] = save_path
        session['list_file'] = list_file
    else:
        session['tmp_file'] = save_path
    return image_name


def delete_session_file():
    """
    删除session保存路径中的图片
    :return:
    """
    image_path = session['tmp_file']
    if image_path:
        if os.path.exists(image_path):
            os.remove(image_path)
        result = {'state': 0}
    else:
        result = {'state': 1}
    return result


def delete_session_list_file():
    """
    删除session中保存的所有图片
    :return: 
    """
    images = session.get('list_file')
    if images:
        for k, v in images.items():
            if os.path.exists(v):
                os.remove(v)
            image_session = session.get(k)
            if image_session:
                session[k] = None
        result = {'state': 0}
    else:
        result = {'state': 1}
    return result


def clear_list_index():
    """
    清理session中的多个文件索引引防止下一次保存文件时删除当前文件
    :return: 
    """
    image_session = session.get('list_file')
    if image_session:
        for key in image_session:
            session[key] = None


def clear_tmp_index():
    """
    清理session中的文件索引防止下一次保存文件时删除当前文件
    :return:
    """
    session['tmp_file'] = None


def read_file(path, fileName):
    """
    读取json文件
    :param path: 文件路径
    :return: 
    """
    data = {}
    file_path = os.path.join(path, fileName)
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        if size > 0:
            with open(file_path) as fs:
                data = json.load(fs, encoding='utf8')
    elif not os.path.exists(path):
        os.makedirs(path)
    return data
