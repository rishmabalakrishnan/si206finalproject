import json
import unittest
import os
import requests


api_key = "9d6fafde-d754-4e78-bdc3-1ff0e16d85d1"

def get_recipes(api_key):
  
    header ={'X-API-KEY': api_key, 'Accept-Version': '1.0.0' }
    url = f'https://api.nookipedia.com/nh/recipes'

    r = requests.get(url, headers = header).text
    recipes_dict = json.loads(r)

    return recipes_dict

# make database

# make recipes table





# main
get_recipes(api_key)
