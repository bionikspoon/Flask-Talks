# coding=utf-8
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,

          'default': DevelopmentConfig}