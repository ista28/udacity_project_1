import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT_KEY = os.environ.get('BLOB_ACCOUNT_KEY')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER_KEY = os.environ.get('BLOB_CONTAINER_KEY')
