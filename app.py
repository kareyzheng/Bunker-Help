from flask import Flask, request, render_template, send_from_directory
import json
import pymysql.cursors

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





if __name__ == '__main__':
    app.run(host='0.0.0.0')