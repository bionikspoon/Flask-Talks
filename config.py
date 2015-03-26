# coding=utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TALKS_PER_PAGE = 50
    COMMENTS_PER_PAGE = 100
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_DEBUG = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_SENDER') or 'admin@app.local'
    MAIL_FLUSH_INTERVAL = 3600  # one hour


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'sqlite:///{}'.format(
        os.path.join(basedir, 'data-dev.sqlite'))
    TALKS_PER_PAGE = 2
    COMMENTS_PER_PAGE = 2
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_DEBUG = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_SENDER') or 'admin@app.local'
    MAIL_FLUSH_INTERVAL = 60  # one minute


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