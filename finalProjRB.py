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

def create_personalities_table(cur, conn, villagers_dict):
    personalities_list = []
    for villager in villagers_dict:
        personality = villagers_dict[villager]['personality']
        if personality not in personalities_list:
            personalities_list.append(personality)
    cur.execute("CREATE TABLE IF NOT EXISTS Personalities (id INTEGER PRIMARY KEY, personality TEXT UNIQUE)")
    for i in range(len(personalities_list)):
        cur.execute("INSERT OR IGNORE INTO Personalities (id,personality) VALUES (?,?)",(i,personalities_list[i]))
    conn.commit()

def create_villagers_table(cur, conn, villagers_dict):
    cur.execute("CREATE TABLE IF NOT EXISTS Villagers (villager_id INTEGER PRIMARY KEY, name TEXT, personality_id INTEGER, birthday TEXT, species TEXT, gender TEXT, catchphrase TEXT)")
    conn.commit()
    for villager in villagers_dict:
        # print(villagers_dict[villager])
        villager_id = villagers_dict[villager]['id']
        # print(villager_id)
        name = villagers_dict[villager]['name']['name-USen']
        # print(name)
        personality = villagers_dict[villager]['personality']
        cur.execute('SELECT id FROM Personalities WHERE Personalities.personality = "' + personality + '"')
        for row in cur:
            personality_id = row[0]
        # print(personality)
        birthday = villagers_dict[villager]['birthday']
        # note: birthday is in the format d/m
        # print(birthday)
        species = villagers_dict[villager]['species']
        # print(species)
        gender = villagers_dict[villager]['gender']
        # print(gender)
        catchphrase = villagers_dict[villager]['catch-phrase']
        # print(catchphrase)
        cur.execute('INSERT OR IGNORE INTO Villagers (villager_id, name, personality_id, birthday, species, gender, catchphrase) VALUES (?, ?, ?, ?, ?, ?, ?)', (villager_id, name, personality_id, birthday, species, gender, catchphrase))
        conn.commit()

def get_fish():
    r = requests.get("https://acnhapi.com/v1/fish").text
    fish_dict = json.loads(r)
    return fish_dict

def create_fish_table(cur, conn, fish_dict):
    cur.execute("CREATE TABLE IF NOT EXISTS Fish (fish_id INTEGER PRIMARY KEY, name TEXT, location TEXT, rarity TEXT, price INTEGER)")
    conn.commit()
    for fish in fish_dict:
        fish_id = fish_dict[fish]['id']
        name = fish_dict[fish]['name']['name-USen']
        location = fish_dict[fish]['availability']['location']
        rarity = fish_dict[fish]['availability']['rarity']
        price = int(fish_dict[fish]['price'])
        cur.execute('INSERT OR IGNORE INTO Fish (fish_id, name, location, rarity, price) VALUES (?, ?, ?, ?, ?)', (fish_id, name, location, rarity, price))
        conn.commit()

def main():
    cur, conn = open_database('acnh.db')
    villagers_dict = get_villagers()
    # print(villagers_dict)
    create_personalities_table(cur, conn, villagers_dict)
    create_villagers_table(cur, conn, villagers_dict)
    fish_dict = get_fish()
    create_fish_table(cur, conn, fish_dict)

if __name__ == "__main__":
    main()
