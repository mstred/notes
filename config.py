from os import environ

db_host = environ.get('DB_HOST', default='localhost')
db_name = environ.get('DB_NAME', default='notes')
db_user = environ.get('DB_USERNAME', default='notes')
db_password = environ.get('DB_PASSWORD', default='notes')
db_port = environ.get('DB_PORT', default='5432')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
