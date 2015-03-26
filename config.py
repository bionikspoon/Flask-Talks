# coding=utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TALKS_PER_PAGE = 50
    COMMENTS_PER_PAGE = 100


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'sqlite:///{}'.format(
        os.path.join(basedir, 'data-dev.sqlite'))
    TALKS_PER_PAGE = 2
    COMMENTS_PER_PAGE = 2


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL') or 'sqlite:///{}'.format(
        os.path.join(basedir, 'test-dev.sqlite'))


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///{}'.format(
        os.path.join(basedir, 'data.sqlite'))


config = {'development': DevelopmentConfig, 'testing': TestingConfig,
          'production': ProductionConfig, 'default': DevelopmentConfig}