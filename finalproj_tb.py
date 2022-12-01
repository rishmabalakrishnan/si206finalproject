import json
import sqlite3
# import unittest
import os
import requests


api_key = "9d6fafde-d754-4e78-bdc3-1ff0e16d85d1"


def get_recipes(api_key):
  
    header ={'X-API-KEY': api_key, 'Accept-Version': '1.0.0'}
    url = f'https://api.nookipedia.com/nh/recipes'

    r = requests.get(url, headers= header).text
    recipes_dict = json.loads(r)

    return recipes_dict

    # do i need to cache my file since my data structure is so long?

def make_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# ''' create recipes table
#     -serial id
#     -item name
#     -availability ['from']
#      "materials": [
    #   {
    #     "name": "wood",
    #     "count": 10
    #   }
# '''
def create_recipes_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS recipes")
    cur.execute("CREATE TABLE IF NOT EXISTS recipes (item_id INTEGER PRIMARY KEY, name TEXT, materials TEXT?????? count INTEGER, availability TEXT)")
conn.commit()



def main():
    # SETUP DATABASE AND TABLE
    cur, conn = make_database('acnh.db')
    create_recipes_table(cur, conn)
    get_recipes(api_key)
