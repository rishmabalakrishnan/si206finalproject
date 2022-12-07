import sqlite3
import os

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
    
def villager_personality_counts(cur, conn):
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 0")
    cranky_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 1")
    jock_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 2")
    peppy_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 3")
    snooty_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 4")
    normal_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 5")
    smug_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 6")
    lazy_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 7")
    sisterly_count = cur.fetchone()[0]
    personalities_dict = {}
    personalities_dict['cranky'] = cranky_count
    personalities_dict['jock'] = jock_count
    personalities_dict['peppy'] = peppy_count
    personalities_dict['snooty'] = snooty_count
    personalities_dict['normal'] = normal_count
    personalities_dict['smug'] = smug_count
    personalities_dict['lazy'] = lazy_count
    personalities_dict['sisterly'] = sisterly_count
    print(personalities_dict)
    sorted_dict = dict(sorted(personalities_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    return sorted_dict

def villager_species_counts(cur, conn):
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 0")
    anteater_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 1")
    anteater_count = cur.fetchone()[0]


def main():
    # need to open database and form a connection
    cur, conn = open_database('acnh.db')
    # calculations:
    # 1. dictionary for most common villager species -> turn this into pie chart
    # 2. dictionary for most common villager personalities -> turn this into pie chart
    # 3. avg selling price for each rarity of fish
    sorted_personality_dict = villager_personality_counts(cur, conn)

if __name__ == "__main__":
    main()