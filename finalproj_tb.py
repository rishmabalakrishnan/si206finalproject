import json
import sqlite3
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


def create_availability_table(recipes_dict, cur, conn, total_count):
    new_count = 0
    avail_list = []
    for recipe in recipes_dict:
        availability = recipe["availability"][0]["from"]
        if availability not in avail_list:
            avail_list.append(availability)
    cur.execute("CREATE TABLE IF NOT EXISTS availability (id INTEGER PRIMARY KEY, availability TEXT UNIQUE)")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM availability")
    availability_count = cur.fetchone()[0]
    # print(availability_count)
    if availability_count < len(avail_list):
        for i in range(availability_count, len(avail_list)):
            if total_count + new_count < 25:
                cur.execute("INSERT OR IGNORE INTO availability (id, availability) VALUES (?,?)",(i,avail_list[i]))
                conn.commit()
                new_count += 1
            else:
                quit()
    
    return new_count


def create_recipes_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS recipes (item_id INTEGER PRIMARY KEY, name TEXT, availability_id INTEGER, wood INTEGER, hardwood INTEGER, softwood INTEGER, stone INTEGER, iron_nugget INTEGER, clay INTEGER, tree_branch INTEGER)")

    conn.commit()

def make_insert_recipes_dict(recipes_dict, cur, conn):
    insert_recipes = {}
    
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
            # item_id = count
            
            # cur.execute("INSERT OR IGNORE INTO recipes (item_id, name, availability_id, wood, hardwood, softwood, stone, iron_nugget, clay, tree_branch) VALUES (?,?,?,?,?,?,?,?,?,?)" , (item_id, name, availability_id, wood, hardwood, softwood, stone, iron_nugget, clay, tree_branch))
            insert_recipes[item_id] = []
            insert_recipes[item_id].append(name)
            insert_recipes[item_id].append(availability_id)
            insert_recipes[item_id].append(wood)
            insert_recipes[item_id].append(hardwood)
            insert_recipes[item_id].append(softwood)
            insert_recipes[item_id].append(stone)
            insert_recipes[item_id].append(iron_nugget)
            insert_recipes[item_id].append(clay)
            insert_recipes[item_id].append(tree_branch)
    count = 0
    for item_id in insert_recipes:
        insert_recipes[item_id].append(count)
        count += 1
    print(len(insert_recipes))

    return insert_recipes


def add_recipes_to_table (insert_recipes_dict, cur, conn, total_count):
    new_count = 0
    cur.execute("SELECT COUNT(*) FROM recipes")
    recipes_count = cur.fetchone()[0]
    for recipe in insert_recipes_dict:
        # print(insert_recipes_dict[recipe])
        # print("new count", new_count)
        insert_item_id = insert_recipes_dict[recipe][-1]
        if (insert_item_id in range(recipes_count, len(insert_recipes_dict) + 1)) and (total_count + new_count < 25):
            insert_name = insert_recipes_dict[recipe][0]
            insert_availability_id = insert_recipes_dict[recipe][1]
            insert_wood = insert_recipes_dict[recipe][2]
            insert_hardwood = insert_recipes_dict[recipe][3]
            insert_softwood = insert_recipes_dict[recipe][4]
            insert_stone = insert_recipes_dict[recipe][5]
            insert_iron_nugget = insert_recipes_dict[recipe][6]
            insert_clay = insert_recipes_dict[recipe][7]
            insert_tree_branch = insert_recipes_dict[recipe][8]
            cur.execute("INSERT OR IGNORE INTO recipes (item_id, name, availability_id, wood, hardwood, softwood, stone, iron_nugget, clay, tree_branch) VALUES (?,?,?,?,?,?,?,?,?,?)" , (insert_item_id, insert_name, insert_availability_id, insert_wood, insert_hardwood, insert_softwood, insert_stone, insert_iron_nugget, insert_clay, insert_tree_branch))
            new_count += 1
            conn.commit()
        else:
            continue
    return new_count

def main():
    cur, conn = make_database('acnh.db')
    recipes_dict = get_recipes(api_key)
    total_count = 0
    total_count += create_availability_table(recipes_dict, cur, conn, total_count)
    print(total_count)
    create_recipes_table(cur, conn)
    to_insert = make_insert_recipes_dict(recipes_dict, cur, conn)
    # print(to_insert)
    total_count += add_recipes_to_table(to_insert, cur, conn, total_count)
    print("new", total_count)

main()