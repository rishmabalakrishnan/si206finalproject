import os
import sqlite3
import matplotlib
import matplotlib.pyplot as plt


# calculate the top 5 materials used and the amount of each material it requires

def get_top_five(cur, conn):
    pass

# the recipes with the most materials 

def get_most_recipes(cur, conn):
    pass

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn



def main():
    cur, conn = open_database('acnh.db')