import requests
import json
import sys

basket_data = None
with open("basket.json", 'r') as f:
    basket_data = json.load(f)

basket = sys.argv.pop(1)

url = "https://getpantry.cloud/apiv1/pantry/7802dc28-b0f7-4f89-994e-3a64af43c771/basket/" + basket

new_basket = requests.post(url, json=basket_data)
print(new_basket.status_code)
