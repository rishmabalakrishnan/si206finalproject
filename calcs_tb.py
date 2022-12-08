import os
import sqlite3
import matplotlib
import matplotlib.pyplot as plt

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_top_three(cur, conn):
    materials_dict ={}

    cur.execute("SELECT COUNT (wood) FROM recipes WHERE wood > 0")
    total_wood = cur.fetchone()[0]
    materials_dict["wood"] = total_wood

    cur.execute("SELECT COUNT (hardwood) FROM recipes WHERE hardwood > 0")
    total_hardwood = cur.fetchone()[0]
    materials_dict["hardwood"] = total_hardwood

    cur.execute("SELECT COUNT (softwood) FROM recipes WHERE softwood > 0")
    total_softwood = cur.fetchone()[0]
    materials_dict["softwood"] = total_softwood
    
    cur.execute("SELECT COUNT (stone) FROM recipes WHERE stone > 0")
    total_stone = cur.fetchone()[0]
    materials_dict["stone"] = total_stone
    
    cur.execute("SELECT COUNT (iron_nugget) FROM recipes WHERE iron_nugget > 0")
    total_iron_nugget = cur.fetchone()[0]
    materials_dict["iron nugget"] = total_iron_nugget

    cur.execute("SELECT COUNT (clay) FROM recipes WHERE clay > 0")
    total_clay = cur.fetchone()[0]
    materials_dict["clay"] = total_clay

    cur.execute("SELECT COUNT (tree_branch) FROM recipes WHERE tree_branch > 0")
    total_tree_branch = cur.fetchone()[0]
    materials_dict["tree branch"] = total_tree_branch

    items = materials_dict.items()
    sorted_materials = sorted(items, key = lambda t: t[1], reverse= True)

    top_three_materials = sorted_materials[0:3]
    print(top_three_materials)
    return top_three_materials

def get_most_availability(cur,conn):
    availability_dict ={}
    cur.execute("SELECT availability.availability FROM availability JOIN recipes ON recipes.availability_id = availability.id")
    recipes_avail = cur.fetchall()
    
    for item in recipes_avail:
        if item[0] not in availability_dict:
            availability_dict[item[0]] = 0
        availability_dict[item[0]] += 1

    obtain_methods = availability_dict.items()
    sorted_methods = (sorted(obtain_methods, key = lambda t: t[1], reverse= True))

    top_methods = sorted_methods[0:10]
    print(top_methods)
    return top_methods

def write_file(top_three_materials, top_availability):
    fh = open("calculationsTB.txt", 'w')
    fh.write("In the game Animal Crossing: New Horizons, the DIY feature allows players to craft items or cook recipes using various materials.\nOut of 263 basic crafting recipes, these are the materials that are required most frequently:\n")
    for material in top_three_materials:
        fh.write(f'{material[0]} is used in {str(material[1])} recipes\n')
    fh.write("\nIn the game, you can obtain these crafting recipes in a variety of ways, such as from specific characters or from message bottles on the beach.\nOut of the 263 basic crafting recipes, these methods are the 10 most common ways of obtaining recipes:\n")
    for avail in top_availability:
        fh.write(f'You can obtain {str(avail[1])} recipes from {avail[0]}\n')

def get_vis1_names(top_three_materials):
    name_list_1 = []

    for material in top_three_materials:
        material_name = material[0]
        name_list_1.append(material_name)
    print(name_list_1)
    return name_list_1

def get_vis1_values(top_three_materials):
    value_list_1 = []

    for material in top_three_materials:
        material_value = material[1]
        value_list_1.append(material_value)
    print(value_list_1)
    return value_list_1

def get_vis2_names(top_methods):
    name_list_2 = []

    for availability in top_methods:
        method_name = availability[0]
        name_list_2.append(method_name)
    print(name_list_2)
    return name_list_2

def get_vis2_values(top_methods):
    value_list_2 = []

    for availability in top_methods:
        method_value = availability[1]
        value_list_2.append(method_value)
    print(value_list_2)
    return value_list_2


def create_visualization1(vis1_names, vis1_values):
    plt.figure()
    fig, ax = plt.subplots()
    ax.set_xlabel('Materials')
    ax.set_ylabel('Number of Recipes')
    plt.bar(vis1_names, vis1_values, color = ["dimgray", "sienna", "darkgray"])
    plt.suptitle('Top Three Required Materials')
    fig.savefig("materials_bar_chart.png")
    plt.show()
    
def create_visualization2(vis2_names, vis2_values):
    plt.figure()
    fig, ax = plt.subplots()
    ax.set_xlabel('Availability')
    ax.set_ylabel('Number of Recipes')
    plt.scatter(vis2_names, vis2_values, color = "darksalmon")
    plt.draw()
    plt.xticks(rotation = 15)
    plt.suptitle('Top Methods of Obtaining Recipes')
    fig.savefig("availability_scatter_plot.png")
    plt.show()

def main():
    cur, conn = open_database('acnh.db')

    top_three_materials = get_top_three(cur, conn)
    top_availability = get_most_availability(cur, conn)

    write_file(top_three_materials, top_availability)

    vis1_names = get_vis1_names(top_three_materials)
    vis1_values = get_vis1_values(top_three_materials)


    vis2_names = get_vis2_names(top_availability)
    vis2_values = get_vis2_values(top_availability)

    create_visualization1(vis1_names, vis1_values)
    create_visualization2(vis2_names, vis2_values)



if __name__ == "__main__":
    main()