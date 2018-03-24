from flask import Flask, request, render_template, redirect, url_for
import pymysql

import gmaps
import googlemaps
import psycopg2


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

@app.route("/Shelter/")
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

@app.route("/map/", methods=['POST'])
def map():
    name = request.form['Name']
    address = request.form['Address']
    city = request.form['City']
    zip = request.form['ZipCode']
    capacity = request.form['Capacity']
    notes = request.form['Notes']
    phone = request.form['Phone']
    return render_template("map.html")

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

    cursor = conn.cursor()

    shelters = "INSERT INTO `shelter` (`name`, `address`, `zipcode`, `city`, `capacity`, " \
               "`resources`, `phone`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(shelters, (name, address, zip, city, capacity, notes, phone))
    conn.commit()

    conn.close()
    gmaps = googlemaps.Client(key="AIzaSyB1Udy3X-6-BGZaJt-SIT0OrvUWo_i4uWs")

    results = gmaps.geocode(address+zip+city)

    for result in results:
        geo = result['geometry']
        lat, lng = geo['location']['lat'], geo['location']['lng']
        position = ("{lat: %s, lng: %s}" % (lat, lng))
    return render_template("map.html", address=address, zip=zip, city=city, position=position)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)