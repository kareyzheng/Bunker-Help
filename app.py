from flask import Flask, request, render_template
import pymysql.cursors

app = Flask(__name__)


def get_database_connection():
    return pymysql.connect(
         host='localhost',
         user='shelter',
         password='password',
         db='shelter_database',
         charset='utf8mb4',
         cursorclass=pymysql.cursors.DictCursor
     )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Shelter/", methods=['POST'])
def shelter():
    return render_template("Shelter.html")

@app.route("/provide")
def provide():
    zipcode = request.form['ZipCode']
    people = request.form['People']

@app.route("/ShelterProvider/")
def shelterprovider():
    print("Success")
    return render_template("ShelterProvider.html")

@app.route('/send/', methods=['POST'])
def send():
    name = request.form['Name']
    address = request.form['Address']
    city = request.form['City']
    zip = request.form['ZipCode']
    capacity = request.form['Capacity']
    notes = request.form['Notes']
    phone = request.form['Phone']

    conn = get_database_connection()

    cursor = conn.cursor
    shelters = "INSERT INTO `shelter` (`name`, `address`, `zipcode`, `city`, `capacity`, `resources`, `phone`) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(shelters, (name, address, zip, city, capacity, notes, phone))
    conn.commit()

    conn.close()
    return render_template("success.html")

@app.route("/success/")
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)