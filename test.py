import random
import requests
import time
from fastapi import Response

API_URL = "http://localhost:8000/prediction"

# Define the range of values for each field
fields_range = {
    "step": (1, 100),
    "type": (1, 3),
    "amount": (0.0, 1000.0),
    "oldbalanceOrg": (0.0, 10000.0),
    "newbalanceOrig": (0.0, 10000.0),
    "oldbalanceDest": (0.0, 10000.0),
    "newbalanceDest": (0.0, 10000.0)
}

# Generate random data for the API fields
def generate_random_data():
    data = {}
    for field, (min_val, max_val) in fields_range.items():
        if field == "type":
            data[field] = random.randint(min_val, max_val)
        else:
            data[field] = round(random.uniform(min_val, max_val), 2)
    return data

# Send a request to the API every 1 second
while True:
    data = generate_random_data()
    response = requests.post(API_URL, json=data)
    result = response.json()
    print(result)
    time.sleep(1)