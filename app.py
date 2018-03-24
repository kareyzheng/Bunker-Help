from flask import Flask, request, render_template, send_from_directory
import json
import pymysql.cursors

app = Flask(__name__)

@app.route('/', methods=['GET'])