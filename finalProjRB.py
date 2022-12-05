import sqlite3
import json
import os
import requests

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_villagers():
    r = requests.get("https://acnhapi.com/v1/villagers").text
    villagers_dict = json.loads(r)
    return villagers_dict

def create_villagers_table(cur, conn, villagers_dict):
    cur.execute("CREATE TABLE IF NOT EXISTS Villagers (villager_id INTEGER PRIMARY KEY, name TEXT, personality TEXT, birthday TEXT, species TEXT, gender TEXT, catchphrase TEXT)")
    conn.commit()
    for villager in villagers_dict:
        # print(villagers_dict[villager])
        villager_id = villagers_dict[villager]['id']
        print(villager_id)

def main():
    cur, conn = open_database('acnh.db')
    villagers_dict = get_villagers()
    # print(villagers_dict)
    create_villagers_table(cur, conn, villagers_dict)

if __name__ == "__main__":
    main()
