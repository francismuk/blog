import os

class Config:
    SECRET_KEY = '1234'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    os.environ['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://francis:1234@localhost/blog'
    os.environ['MAIL_USERNAME'] = 'user@example.com'
    os.environ['MAIL_PASSWORD'] = 'aeb72hasow82ajl'
    os.environ['SECRET_KEY'] = '1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blog'

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='mukuha58@gmail.com'
    MAIL_PASSWORD='fwm284fwm'



class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blog'

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blog'

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blog'

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blog'



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
