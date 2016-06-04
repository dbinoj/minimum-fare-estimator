#!/usr/bin/env python

from uber_api import ride_requests, config
import requests
from flask import Flask, jsonify

# Set Application name
app = Flask('uber_rides_application')
uber_api = 'https://api.uber.com/v1/'


cfg = config.settings.get_config()
server_token = cfg['server_token']

@app.route('/fare_estimate/<float:latitude>,<float:longitude>')
def get_estimate(latitude, longitude):
    estimate_url = '%s%s' % (uber_api, 'estimates/price')
    parameters = {
        'server_token': server_token,
        'start_latitude': latitude,
        'start_longitude': longitude,
        'end_latitude': 12.914282,
        'end_longitude': 77.651579,
        'seat_count': 1
    }
    #return jsonify(parameters)
    response = requests.get(estimate_url, params=parameters)
    data = response.json()
    return jsonify(data)


@app.route('/get_products')
def get_products():
    products_url = '%s%s' % (uber_api, 'products')
    parameters = {
        'server_token': server_token,
        'latitude': 37.775818,
        'longitude': -122.418028,
    }
    response = requests.get(products_url, params=parameters)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
     app.run(debug=True)
