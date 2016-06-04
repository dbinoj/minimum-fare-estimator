import yaml
import requests

url = 'https://api.uber.com/v1/products'

parameters = {
    'server_token': 'NPALVDnUaq6dOOIQ8FHAO8-4lggXw16xGDRWOWn1',
    'latitude': 37.775818,
    'longitude': -122.418028,
}

response = requests.get(url, params=parameters)
data = response.json()

print data
