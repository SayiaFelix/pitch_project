import os

class Config:

    SECRET_KEY = 'f2GDBACdGn5ZGx$A!gC[:+*/b.JS?('
    SQLALCHEMY_DATABASE_URI = 'postgres://lybbhvznzgrbxa:bed0b7b6f15b58eeb87996fde36aa4ae79bc0bd2bb1f7a579582334afc7ccca4@ec2-3-217-113-25.compute-1.amazonaws.com:5432/d8so18ov06lcno'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jaysafu@localhost/pitcheslist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'SiR Felix Pitch Hub!'
    SENDER_EMAIL = 'sayiafelix18@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    class ProdConfig(Config):
     uri = os.getenv('DATABASE_URL')
     if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
        
        SQLALCHEMY_DATABASE_URI=uri
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jaysafu@localhost/pitches_test'
  

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jaysafu@localhost/pitcheslist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}