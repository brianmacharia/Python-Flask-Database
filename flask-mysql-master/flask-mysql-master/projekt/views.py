from flask import render_template
from projekt import app
from projekt import mysql

@app.route('/')
def index():
    text = "Hello!"
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from table")
    data = cursor.fetchall()
    return render_template('index.html', text = text, data = data)
