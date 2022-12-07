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

def make_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_recipes_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS recipes (item_id INTEGER PRIMARY KEY, name TEXT, wood INTEGER, hardwood INTEGER, softwood INTEGER, stone INTEGER, iron_nugget INTEGER, clay INTEGER, tree_branch INTEGER)")

    conn.commit()


def add_recipes_to_table (recipes_dict, cur, conn):
    
    for recipe in recipes_dict:
        item_id = recipe["serial_id"]
        name = recipe["name"]

    # exclude wallpaper, flooring, wreaths, wands
        if "wall" in name or "flooring" in name or "wreath" in name or "wand" in name:
            continue

        for material in recipe["materials"]:

            material_list= ["wood", "hardwood", "softwood", "tree_branch", "clay", "iron_nugget", "stone"]
            if material["name"] not in material_list:
                continue
            
            # recipe_materials = {}
            if material["name"] == "wood":
                # recipe_materials[material] = material["count"]
                # print(recipe_materials[material])
                wood = material["count"]
            else:
                wood = 0

            # print(recipe_materials[wood])
        
            if material["name"] == "hardwood":
                hardwood = material["count"]
            else:
                hardwood = 0

            if material["name"] == "softwood":
                softwood = material["count"]
            else:
                softwood = 0

            if material["name"] == "stone":
                stone = material["count"]
            else:
                stone = 0
            
            if material["name"] == "iron nugget":
                iron_nugget = material["count"]
            else:
                iron_nugget = 0

            if material["name"] == "clay":
                clay = material["count"]
            else:
                clay = 0

            if material["name"] == "tree branch":
                tree_branch = material["count"]
            else:
                tree_branch = 0

            cur.execute("INSERT OR IGNORE INTO recipes (item_id, name, wood, hardwood, softwood, stone, iron_nugget, clay, tree_branch) VALUES (?,?,?,?,?,?,?,?,?)",(item_id, name, wood, hardwood, softwood, stone, iron_nugget, clay, tree_branch))
        conn.commit()


def main():
    cur, conn = make_database('acnh.db')
    create_recipes_table(cur, conn)
    recipes_dict = get_recipes(api_key)
    add_recipes_to_table(recipes_dict, cur, conn)

main()