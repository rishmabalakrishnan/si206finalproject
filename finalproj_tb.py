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


def create_availability_table(recipes_dict, cur, conn):
    avail_list = []
    for recipe in recipes_dict:
        availability = recipe["availability"][0]["from"]
        if availability not in avail_list:
            avail_list.append(availability)
    cur.execute("CREATE TABLE IF NOT EXISTS availability (id INTEGER PRIMARY KEY, availability TEXT UNIQUE)")
    for i in range(len(avail_list)):
        cur.execute("INSERT OR IGNORE INTO availability (id, availability) VALUES (?,?)",(i,avail_list[i]))
    conn.commit()


def create_recipes_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS recipes (item_id INTEGER PRIMARY KEY, name TEXT, availability_id INTEGER, wood INTEGER, hardwood INTEGER, softwood INTEGER, stone INTEGER, iron_nugget INTEGER, clay INTEGER, tree_branch INTEGER)")

    conn.commit()

def add_recipes_to_table (recipes_dict, cur, conn):

    for recipe in recipes_dict:
        item_id = recipe["serial_id"]
        name = recipe["name"]

        cur.execute("SELECT id FROM availability WHERE availability = ?", (recipe["availability"][0]["from"],))
        availability_id = int(cur.fetchone()[0])

    # exclude wallpaper, flooring, wreaths, wands
        if "wall" in name or "flooring" in name or "wreath" in name or "wand" in name:
            continue
        
        material_list= ["wood", "hardwood", "softwood", "tree branch", "clay", "iron nugget", "stone"]

        for material in recipe["materials"]:
        #     material_name = material["name"]
        #     material_count = material['count']
        #     if material_name in material_list:
        #         recipe_materials[material_name] = material_count #recipe_materials.get(material_name, 0) + 1 
        # print(recipe_materials)

            if material["name"] not in material_list:
                continue
            
            if material["name"] == "wood":
                wood = material["count"]
            else:
                wood = 0
        
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

            cur.execute("INSERT OR IGNORE INTO recipes (item_id, name, availability_id, wood, hardwood, softwood, stone, iron_nugget, clay, tree_branch) VALUES (?,?,?,?,?,?,?,?,?,?)" , (item_id, name, availability_id, wood, hardwood, softwood, stone, iron_nugget, clay, tree_branch))
        conn.commit()

def main():
    cur, conn = make_database('acnh.db')
    recipes_dict = get_recipes(api_key)
    total_count = 0
    create_availability_table(recipes_dict, cur, conn)
    create_recipes_table(cur, conn)
    add_recipes_to_table(recipes_dict, cur, conn)

main()