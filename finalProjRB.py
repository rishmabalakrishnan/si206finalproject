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

def create_species_table(cur, conn, villagers_dict):
    species_list = []
    for villager in villagers_dict:
        species = villagers_dict[villager]['species']
        if species not in species_list:
            species_list.append(species)
    cur.execute("CREATE TABLE IF NOT EXISTS Species (id INTEGER PRIMARY KEY, species TEXT UNIQUE)")
    for i in range(len(species_list)):
        cur.execute("INSERT OR IGNORE INTO Species (id,species) VALUES (?,?)",(i,species_list[i]))
    conn.commit()

def create_villagers_table(cur, conn, villagers_dict):
    cur.execute("CREATE TABLE IF NOT EXISTS Villagers (villager_id INTEGER PRIMARY KEY, name TEXT, personality_id INTEGER, birthday TEXT, species_id INTEGER, gender INTEGER, catchphrase TEXT)")
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
        cur.execute('SELECT id FROM Species WHERE Species.species = "' + species + '"')
        for row in cur:
            species_id = row[0]
        # print(species)
        gender = villagers_dict[villager]['gender']
        if gender == 'Male':
            gender = 0
        else:
            gender = 1
        # print(gender)
        catchphrase = villagers_dict[villager]['catch-phrase']
        # print(catchphrase)
        cur.execute('INSERT OR IGNORE INTO Villagers (villager_id, name, personality_id, birthday, species_id, gender, catchphrase) VALUES (?, ?, ?, ?, ?, ?, ?)', (villager_id, name, personality_id, birthday, species_id, gender, catchphrase))
        conn.commit()

def get_fish():
    r = requests.get("https://acnhapi.com/v1/fish").text
    fish_dict = json.loads(r)
    return fish_dict

def create_location_table(cur, conn, fish_dict):
    locations_list = []
    for fish in fish_dict:
        location = fish_dict[fish]['availability']['location'].split()[0]
        if location not in locations_list:
            locations_list.append(location)
    cur.execute("CREATE TABLE IF NOT EXISTS Locations (id INTEGER PRIMARY KEY, location TEXT UNIQUE)")
    for i in range(len(locations_list)):
        cur.execute("INSERT OR IGNORE INTO Locations (id,location) VALUES (?,?)",(i,locations_list[i]))
    conn.commit()

def create_rarity_table(cur, conn, fish_dict):
    rarity_list = []
    for fish in fish_dict:
        rarity = fish_dict[fish]['availability']['rarity']
        if rarity not in rarity_list:
            rarity_list.append(rarity)
    cur.execute("CREATE TABLE IF NOT EXISTS Rarities (id INTEGER PRIMARY KEY, rarity TEXT UNIQUE)")
    for i in range(len(rarity_list)):
        cur.execute("INSERT OR IGNORE INTO Rarities (id,rarity) VALUES (?,?)",(i,rarity_list[i]))
    conn.commit()

def create_fish_table(cur, conn, fish_dict):
    cur.execute("CREATE TABLE IF NOT EXISTS Fish (fish_id INTEGER PRIMARY KEY, name TEXT, location_id INTEGER, rarity_id INTEGER, price INTEGER)")
    conn.commit()
    for fish in fish_dict:
        fish_id = fish_dict[fish]['id']
        name = fish_dict[fish]['name']['name-USen']
        location = fish_dict[fish]['availability']['location']
        cur.execute('SELECT id FROM Locations WHERE Locations.location = "' + location + '"')
        for row in cur:
            location_id = row[0]
        rarity = fish_dict[fish]['availability']['rarity']
        cur.execute('SELECT id FROM Rarities WHERE Rarities.rarity = "' + rarity + '"')
        for row in cur:
            rarity_id = row[0]
        price = int(fish_dict[fish]['price'])
        cur.execute('INSERT OR IGNORE INTO Fish (fish_id, name, location_id, rarity_id, price) VALUES (?, ?, ?, ?, ?)', (fish_id, name, location_id, rarity_id, price))
        conn.commit()

def main():
    cur, conn = open_database('acnh.db')
    villagers_dict = get_villagers()
    # print(villagers_dict)
    create_personalities_table(cur, conn, villagers_dict)
    create_species_table(cur, conn, villagers_dict)
    create_villagers_table(cur, conn, villagers_dict)
    fish_dict = get_fish()
    create_location_table(cur, conn, fish_dict)
    create_rarity_table(cur, conn, fish_dict)
    create_fish_table(cur, conn, fish_dict)

if __name__ == "__main__":
    main()
