from flask import Flask, request, render_template, send_from_directory
import json
# import pymysql.cursors

app = Flask(__name__)


def get_database_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        db='todo_database',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
     )




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Shelter/")
def shelter():
    return render_template("Shelter.html")

@app.route("/ShelterProvider/")
def shelterprovider():
    return render_template("ShelterProvider.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)