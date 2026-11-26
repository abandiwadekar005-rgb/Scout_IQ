import sqlite3
from database import PlayerDatabase

db = PlayerDatabase()

# checks if every player from the CSV is loaded into the database. expect 21
print("T1:", db.load_csv("data/synthetic_players.csv"))                    
db.load_csv("data/synthetic_players.csv")

# checks if it loading a second time replaces the players instead of duplicating them. expect 21
print("T2:", len(db.get_all_players()))   

# checks if a valid player can be found by name. expect 1
print("T3:", db.get_player_by_name("Poacher A")["player_id"])              

# checks an unknown name returns None instead of crashing. expect None
print("T4:", db.get_player_by_name("Nonexistent Player"))              

# checks if an empty search is handled safely, expect None
print("T5:", db.get_player_by_name(""))              

# checks if the search ignores capital letters. expect Poacher A                      
print("T6:", db.get_player_by_name("poacher a")["name"])

table_sql = sqlite3.connect("scoutiq.db").execute(
    "SELECT sql FROM sqlite_master WHERE name = 'players'").fetchone()[0]

#check if player_id is the primary key, so every player stays unique. expect True
print("T7:", "PRIMARY KEY" in table_sql)          