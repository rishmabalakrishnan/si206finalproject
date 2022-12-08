import sqlite3
import os
import matplotlib
import matplotlib.pyplot as plt

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
    
def villager_personality_counts(cur, conn):
    personalities_dict = {}
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 0")
    personalities_dict['cranky'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 1")
    personalities_dict['jock'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 2")
    personalities_dict['peppy'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 3")
    personalities_dict['snooty'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 4")
    personalities_dict['normal'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 5")
    personalities_dict['smug'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 6")
    personalities_dict['lazy'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE personality_id = 7")
    personalities_dict['sisterly'] = cur.fetchone()[0]
    
    
    print(personalities_dict)
    sorted_dict = dict(sorted(personalities_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    return sorted_dict

def villager_species_counts(cur, conn):
    species_dict = {}
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 0")
    species_dict['anteater'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 1")
    species_dict['bear'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 2")
    species_dict['bird'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 3")
    species_dict['bull'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 4")
    species_dict['cat'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 5")
    species_dict['cub'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 6")
    species_dict['chicken'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 7")
    species_dict['cow'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 8")
    species_dict['alligator'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 9")
    species_dict['deer'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 10")
    species_dict['dog'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 11")
    species_dict['duck'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 12")
    species_dict['elephant'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 13")
    species_dict['frog'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 14")
    species_dict['goat'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 15")
    species_dict['gorilla'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 16")
    species_dict['hamster'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 17")
    species_dict['hippo'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 18")
    species_dict['horse'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 19")
    species_dict['koala'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 20")
    species_dict['kangaroo'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 21")
    species_dict['lion'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 22")
    species_dict['monkey'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 23")
    species_dict['mouse'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 24")
    species_dict['octopus'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 25")
    species_dict['ostrich'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 26")
    species_dict['eagle'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 27")
    species_dict['penguin'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 28")
    species_dict['pig'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 29")
    species_dict['rabbit'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 30")
    species_dict['rhino'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 31")
    species_dict['sheep'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 32")
    species_dict['squirrel'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 33")
    species_dict['tiger'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Villagers WHERE species_id = 34")
    species_dict['wolf'] = cur.fetchone()[0]
    
    print(species_dict)
    sorted_dict = dict(sorted(species_dict.items(), key=lambda item: item[1], reverse=True))
    sorted_dict = dict(list(sorted_dict.items())[0: 5]) 
    print(sorted_dict)
    return sorted_dict

def avg_prices_by_rarity(cur, conn):
    prices_dict = {}
    cur.execute("SELECT price FROM Fish WHERE rarity_id = 0")
    prices_dict['common'] = []
    for row in cur:
        prices_dict['common'].append(row[0])
    cur.execute("SELECT price FROM Fish WHERE rarity_id = 1")
    prices_dict['uncommon'] = []
    for row in cur:
        prices_dict['uncommon'].append(row[0])
    cur.execute("SELECT price FROM Fish WHERE rarity_id = 2")
    prices_dict['rare'] = []
    for row in cur:
        prices_dict['rare'].append(row[0])
    cur.execute("SELECT price FROM Fish WHERE rarity_id = 3")
    prices_dict['ultra-rare'] = []
    for row in cur:
        prices_dict['ultra-rare'].append(row[0])

    print(prices_dict)
    avg_prices = {}
    avg_prices['common'] = sum(prices_dict['common']) / len(prices_dict['common'])
    avg_prices['uncommon'] = sum(prices_dict['uncommon']) / len(prices_dict['uncommon'])
    avg_prices['rare'] = sum(prices_dict['rare']) / len(prices_dict['rare'])
    avg_prices['ultra-rare'] = sum(prices_dict['ultra-rare']) / len(prices_dict['ultra-rare'])
    print(avg_prices)
    return avg_prices

def output(personality_dict, species_dict, avg_fish_prices):
    fh = open("calculationsRB.txt", 'w')
    fh.write("Here are all the villager personalities, in order from most frequent to least frequent:\n")
    for personality in personality_dict:
        fh.write(personality + ": " + str(personality_dict[personality]) + " villagers\n")
    fh.write("\nHere are the top 5 villager species by frequency:\n")
    for species in species_dict:
        fh.write(species + ": " + str(species_dict[species]) + " villagers\n")
    fh.write("\nHere are the average selling prices for each rarity of fish:\n")
    for rarity in avg_fish_prices:
        fh.write(rarity + ": " + str(round(avg_fish_prices[rarity], 2)) + " bells\n")
    fh.close()

def personality_bar_chart(pers_dict):
    personalities = list(pers_dict.keys())
    frequencies = list(pers_dict.values())
    plt.figure()
    fig, ax = plt.subplots()
    ax.set_xlabel('Personality')
    ax.set_ylabel('Number of Villagers')
    plt.bar(personalities, frequencies, color=['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black'])
    plt.suptitle('Frequencies of Villager Personalities')
    fig.savefig("personality_bar_chart.png")
    plt.show()

def species_bar_chart(spec_dict):
    species = list(spec_dict.keys())
    frequencies = list(spec_dict.values())
    plt.figure()
    fig, ax = plt.subplots()
    ax.set_xlabel('Species')
    ax.set_ylabel('Number of Villagers')
    plt.bar(species, frequencies, color=['red', 'orange', 'yellow', 'green', 'blue'])
    plt.suptitle('Top 5 Villager Species')
    fig.savefig("species_bar_chart.png")
    plt.show()

def fish_line_graph(fish_dict):
    rarities = list(fish_dict.keys())
    averages = list(fish_dict.values())
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(rarities, averages, color='purple')
    ax.set_xlabel('Rarity of Fish')
    ax.set_ylabel('Average Selling Price (bells)')
    ax.set_title('Rarity vs Average Selling Price of Fish')
    ax.grid()
    fig.savefig("fish_line_graph.png")
    plt.show()

def main():
    # need to open database and form a connection
    cur, conn = open_database('acnh.db')
    # calculations (write everything to txt file):
    # 1. dictionary for most common villager personalities -> turn this into bar chart
    # 2. dictionary for most common villager species -> turn this into pie chart
    # 3. avg selling price for each rarity of fish
    sorted_personality_dict = villager_personality_counts(cur, conn)
    sorted_species_dict = villager_species_counts(cur, conn)
    avg_fish_prices = avg_prices_by_rarity(cur, conn)
    output(sorted_personality_dict, sorted_species_dict, avg_fish_prices)
    personality_bar_chart(sorted_personality_dict)
    species_bar_chart(sorted_species_dict)
    fish_line_graph(avg_fish_prices)

if __name__ == "__main__":
    main()