from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database_name'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_CHARSET'] = 'utf8'
app.secret_key = 'random-secret-code'
mysql.init_app(app)
from projekt import views
