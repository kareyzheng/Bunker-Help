from flask import Flask, request, render_template, send_from_directory
import json
# import pymysql.cursors

app = Flask(__name__)


#
# def get_database_connection():
#     return pymysql.connect(
#         host='localhost',
#         user='shelter',
#         password='password',
#         db='shelter_database',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        address = request.form['Adress']
        city = request.form['City']
        zip = request.form['ZipCode']
        capacity = request.form['Capacity']
        notes = request.form['Notes']
        print("Success")
    return render_template("test.html", address=address, city=city, zip=zip,capacity=capacity)
    print("Fail")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Shelter/", methods=['POST'])
def shelter():
    return render_template("Shelter.html")


def create():
    name = request.headers['Content']
    conn = get_database_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO `todo` (`item`) VALUES (%s);"
            cursor.execute(sql, (name))
        conn.commit()
    except Exception as e:
        print('ERROR', e)
        conn.close()
        return str({'result': 'failure'}), 500

    conn.close()
    return str({'result': 'success'})


@app.route("/ShelterProvider/")
def shelterprovider():
    print("Success")
    return render_template("ShelterProvider.html")

@app.route("/success/")
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)