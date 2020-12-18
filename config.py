import os

class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/patients'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/doctors'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY= '098765'

#  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'nyambucindy0@gmail.com'
    MAIL_PASSWORD = 'gitz254*'
    SENDER_EMAIL = 'nyambucindy0@gmail.com'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/patients'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/doctors'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gutz254@localhost/pitches_test'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gutz254@localhost/pitches_test'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/patients'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/doctors'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}