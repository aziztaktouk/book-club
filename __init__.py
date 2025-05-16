from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mysql_connector import MySQL

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE'] = 'book_club'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)
bcrypt = Bcrypt(app)

from book_club import routes
