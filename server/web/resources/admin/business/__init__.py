# -*- coding: utf-8 -*-
import os
from .. import api_path as last_path

api_path = last_path + 'business/'

dir_path = os.path.abspath(os.path.dirname(__file__))
UPLOAD_ROOT_PATH = os.path.join(dir_path, '../../../upload')
SAVE_FILE_ROOT_PATH = os.path.join(dir_path, '../../../file_config')
