#Returns a json of key value pairs: {item_id : gil_velocity} sorted by descending gil_velocity
#gil_velocity is defined as the gross gil in sales per day times sales velocity per day over the defined time period (2 weeks)

import json
import requests

days = 14 #Get data from the last 14 days
from_time = days * 86400000 #Time in milliseconds

# Replace YOUR_API_KEY with your Universalis API key
#API_KEY = 'YOUR_API_KEY'

# Set up the request headers with your API key
headers = {
        #'X-API-Key': API_KEY,
        }

# Set up the request parameters to retrieve the market listings for the most recently updated items on the Sargatanas server
params = {
        'world': 'Sargatanas',
        'entries': '200',
        }

# Retrieve the market listings from the Universalis API
response = requests.get(f'https://universalis.app/api/v2/extra/stats/most-recently-updated', headers=headers, params=params)
data = response.json()

# Create a list of comma seperated item ids
item_id_list=""
for item in data['items']:
    item_id_list += str(item['itemID']) + ", "

#Get sale history for each item
params['statsWithin']=from_time
params['entriesWithin']=from_time
params['entriesToReturn'] = 999999
del params['entries']
world = params['world']
del params['world']
response = requests.get(f'https://universalis.app/api/v2/history/{world}/{item_id_list}', headers = headers, params=params)
data = response.json()

#Create a list of gross gil velocity
gil_velocity = {}
for item in data['items']:
    gil_prices = []
    item_dict = data['items'][item]
    for entry in item_dict['entries']:
        l = [entry['pricePerUnit']] * entry['quantity']
        gil_prices.extend(l)
    gil_prices.sort()
    mid = len(gil_prices) // 2
    # Find median price, multiply by sales velocity
    gil_velocity[item] = ((gil_prices[mid] + gil_prices[~mid]) / 2) * item_dict['regularSaleVelocity']

# Sort the list by trade volume in descending order and print the results
sorted_gil_velocity = dict(sorted(gil_velocity.items(), key=lambda x: x[1], reverse=True))

sorted_gil_velocity = json.dumps(sorted_gil_velocity)
print(sorted_gil_velocity)
