# -*- coding: utf-8 -*-
from datetime import timedelta
from flask import Flask, request, send_from_directory
# from werkzeug.utils import import_string
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api

from config import config, JsonConfig
from .models.model import db
import os


# bps = [
# ]


def create_app(config_name):
    app_ = Flask(__name__)
    app_.config.from_object(config[config_name])
    db.init_app(app_)
    # app_.permanent_session_lifetime = timedelta(**JsonConfig['SESSION_TIME'])
    # for path in bps:
    #     bp = import_string(path['import_path'])
    #     app_.register_blueprint(bp, url_prefix=path['url_prefix'])
    return app_


app = create_app(JsonConfig['ENV'])
api = Api(app)
auth = HTTPBasicAuth()


@app.route('/api/upload/<path:upload_path>', methods=['GET'])
def upload_view(upload_path):
    if '../' in upload_path:
        return '{"status": 404, "message": "文件名不允许有../存在"}', 404, {'Content-Type': 'application/json;charset=utf-8'}
    return send_from_directory(os.path.join(app.root_path, 'upload'), upload_path)

@app.route('/robots.txt', methods=["GET"])
def robots_view():
    return "404", 404

@app.errorhandler(404)
def error_handler(err):
    url_path = request.path
    if url_path.startswith('/admin'):
        return send_from_directory(app.root_path, 'admin.html')
    elif url_path.startswith('/api') or url_path.startswith('/admin/upload') or url_path.startswith('/static'):
        return '{"status": 404, "message": "页面不存在"}', 404, {'Content-Type': 'application/json;charset=utf-8'}
    return send_from_directory(app.root_path, 'index.html')

from . import api_router
