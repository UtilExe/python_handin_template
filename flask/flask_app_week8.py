from flask import Flask, jsonify, abort, request
import random
import sqlalchemy as s_a
import pandas as pd

app = Flask(__name__)

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db/cars"
engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
connection = engine.connect()

@app.route('/cars/<int:id>', methods=['GET'])
def retrieveCarById(id):
    query = 'select * from the_cars where id = ' + str(id)
    resultProxy= connection.execute(query)
    resultSet = resultProxy.fetchall()
    car = {
        'make': '',
        'model': '',
        'year': '',
        'gas_pr_km': ''
    }
    for result in resultSet:
        # skipping id, so starting from 1.
        car["make"] = result[1]
        car["model"] = result[2]
        car["year"] = result[3]
        car['gas_pr_km'] = result[4]
        
    return jsonify(car)

# Lav et POST-endpoint "cars/add" som tilføjer en ny bil til database ved følgende JSON-format:
# {
#   "make": "MAKE_HERE",
#   "model": "MODEL_HERE",
#   "year": XXXX,
#   "gas_pr_km": "GAS_HERE"
# }

@app.route('/cars/add/', methods=['POST'])
def createCar():
    if not request.json or not 'make' or not 'model' or not 'year' or not 'gas_pr_km' in request.json:
        abort(400)
        
    # My own way to handle to insert to the last ID, since we don't have auto-increment on id. dunno how to get that from pandas on the other file.
    select_query = 'SELECT MAX(id) FROM the_cars;'
    resultProxy = connection.execute(select_query)
    resultSet = resultProxy.fetchall()
    id = 0
    for result in resultSet:
        id = int(result[0]) +1
    
    # Now we prepare the requests
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    gas_pr_km = request.json['gas_pr_km']
    
    # Let's execute our data into the table
    insert_query = "INSERT INTO the_cars (id, make, model, year, gas_pr_km) VALUES (%s, %s, %s, %s, %s)"
    resultProxy = connection.execute(insert_query, (id, make, model, year, gas_pr_km))
    return jsonify(f'Succesfully inserted the car with the following data: {make} {model} {year} {gas_pr_km}, to the database.')