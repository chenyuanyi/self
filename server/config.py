# -*- coding: utf-8 -*-
import os
import json

DirPath = os.path.abspath(os.path.dirname(__file__))
defaultConfig = DirPath + "/conf/config-base.json"
ConfigFile = os.environ.get("CONFIG_FILE", defaultConfig)

with open(defaultConfig, 'r') as fd:
    defaultJsonConfig = json.load(fd, encoding="utf8")
try:
    with open(ConfigFile, 'r') as fd:
        JsonConf = json.load(fd, encoding="utf8")
    for key in JsonConf:
        defaultJsonConfig[key] = JsonConf[key]
    JsonConfig = defaultJsonConfig
except:
    JsonConfig = defaultJsonConfig


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'ordering_system'
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = JsonConfig['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


ISBASE64 = 0

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
