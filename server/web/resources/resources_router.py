# -*- coding: utf-8 -*-
"""
Created by Linjianhui on 2017/3/29
"""
from web import api, app
from web.common.excel_tool import ExcelTool
from .admin import admin_router

@app.route('/api/download/<string:type_name>', methods=['GET'])
def download_excel_template(type_name):
    return ExcelTool().download_template_file(type_name)
