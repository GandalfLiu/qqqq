import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_database_uri(DATABASE):
    db = DATABASE.get('DATABASE') or 'mysql'
    driver = DATABASE.get('DRIVER') or 'pymysql'
    user = DATABASE.get('USER') or 'root'
    password = DATABASE.get('PASSWORD') or '960417'
    hort = DATABASE.get('HORT') or '127.0.0.1'
    port = DATABASE.get('PORT') or '3306'
    databasename = DATABASE.get('DATABASENAME') or 'HelloFlask'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,user,password,hort,port,databasename)

class BaseConfig():
    DEBUG = False
    TESTING = False
    SECRET_KEY = '()&**856789&^%^&*(^5678&^&*(&'
    SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR,'develop.db')

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR,'testing.db')

class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR,'staging.db')

class ProductConfig(BaseConfig):
    DATABASE = {
        'DATABASE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'960417',
        'HORT':'127.0.0.1',
        'PORT':'3306',
        'DATABASENAME':'FlaskTest',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

config = {
    'develop':DevelopConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'product':ProductConfig,
    'default':DevelopConfig
}