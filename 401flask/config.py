import os
from datetime import timedelta

# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    WTF_CSRF_ENABLED = False
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/project/stocks'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = timedelta(days=14)
      # Flask-Mail Configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='')
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True