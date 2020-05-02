import os

DEBUG = os.environ.get('DEBUG', True)
SSL = os.environ.get('SSL', False)
SECRET_KEY = os.environ.get('SECRET', 'test')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['*'])

DB_NAME = os.environ.get('DB_NAME', 'postgres')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT', '5432')
