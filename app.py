from flask import Flask, request, render_template
import pymysql
import os

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
def geo(address):
    gmaps = googlemaps.Client(key="AIzaSyB1Udy3X-6-BGZaJt-SIT0OrvUWo_i4uWs")

    results = gmaps.geocode(address)

    for result in results:
        geo = result['geometry']
        lat, lng = geo['location']['lat'], geo['location']['lng']
        position = ("{lat: %s, lng: %s}" % (lat, lng))
    return(position)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Shelter/")
def shelter():
    return render_template("Shelter.html")

@app.route("/provide/", methods=['POST'])
def provide():
    halfAddress = request.form['AddressH']
    zip = request.form['ZipCodeH']
    people = request.form['People']
    city = request.form['CityH']
    conn = get_database_connection()
    address = halfAddress+" " + zip+" " + city
    print(address)
    position = geo(address)
    print(position)
    return render_template("ShelterSeekerMap .html", position=position)


'''
    #cursor = conn.cursor()
    avail = "SELECT address FROM shelter;"
    cursor.execute(avail)
    address = [item['address'] for item in cursor.fetchall()]
    avail = "SELECT city FROM shelter;"
    city = [item['city'] for item in cursor.fetchall()]
    avail = "SELECT zipcode FROM shelter;"
    city = [item['zipcode'] for item in cursor.fetchall()]
    def iterate():
        for i in address{}
    #list_matches = match.replace(",", os.linesep)

    #if match == "()":
    #    avail = "SELECT * FROM shelter WHERE city=%s AND capacity>=%s;"
    #    cursor.execute(avail, (zipcode, people))
    #    match = cursor.fetchall()


    #conn.close()'''


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
    halfAddress = request.form['Address']
    city = request.form['City']
    zip = request.form['ZipCode']
    capacity = request.form['Capacity']
    notes = request.form['Notes']
    phone = request.form['Phone']
    address = halfAddress+" " + zip+" " + city
    conn = get_database_connection()

    cursor = conn.cursor()

    shelters = "INSERT INTO `shelter` (`name`, `address`, `zipcode`, `city`, `capacity`, " \
               "`resources`, `phone`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(shelters, (name, address, zip, city, capacity, notes, phone))
    conn.commit()

    conn.close()

    position = geo(address)

    return render_template("ShelterProviderMap.html", address=address, zip=zip, city=city, position=position)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)