import sqlite3 #importing SQlite3 to manage data
import pandas as pd

DB_PATH = "scoutiq.db"

class PlayerDatabase:
    # Stores the players and lets other modules retrieve them.

    def __init__(self, db_path=DB_PATH):
        #This remember which database file every method should use.
        self.db_path = db_path

    def create_players_table(self, df):
    #Create the players table (if missing) with player_id as the primary key.
        create_table_sql = pd.io.sql.get_schema(df, "players", keys="player_id")
        create_table_sql = create_table_sql.replace("CREATE TABLE", "CREATE TABLE IF NOT EXISTS", 1)
        conn = sqlite3.connect(self.db_path)
        conn.execute(create_table_sql)
        conn.commit()
        conn.close()

    def load_csv(self, csv_path):
        # Replace all players with those in the CSV. Returns how many were loaded.
        df = pd.read_csv(csv_path)
        self.create_players_table(df)
        conn = sqlite3.connect(self.db_path)    
        conn.execute("DELETE FROM players")   # clear old rows so IDs are not duplicated       
        df.to_sql("players", conn, if_exists="append", index=False)
        conn.commit()
        conn.close()
        return len(df)

    def get_all_players(self):
        #Return every player as a DataFrame.
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql("SELECT * FROM players", conn)
        conn.close()
        return df

    def get_player_by_name(self, name):
        #Return one player's row (ignoring capital letters), or None if not found.
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql(
            "SELECT * FROM players WHERE name = ? COLLATE NOCASE",
            conn, params=(name,)
        )
        conn.close()
        return None if df.empty else df.iloc[0]


if __name__ == "__main__":
    db = PlayerDatabase()
    n = db.load_csv("data/synthetic_players.csv")
    print(f"Loaded {n} players into {DB_PATH}")

