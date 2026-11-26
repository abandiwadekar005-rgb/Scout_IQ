from database import PlayerDatabase
from preprocessing import clean_players

raw = PlayerDatabase().get_all_players()


def kept(df, name):
    # True if the named player survives validation.
    return name in clean_players(df)["name"].values


def changed(name, column, value):
    # A copy of the players with one value changed for one player.
    df = raw.copy()
    df.loc[df["name"] == name, column] = value
    return df

# checks if all 21 players go in and the 3 invalid ones are removed. expect 18
print("T1:", len(clean_players(raw)))

# checks if a valid player is kept. expect True
print("T2:", kept(raw, "Poacher A"))

# checks if a player with only 50 minutes is removed. expect False
print("T3:", kept(raw, "Low Minutes Player"))

# checks if a player with a missing stat is removed. expect False
print("T4:", kept(raw, "Null Stat Player"))

# checks if a player with a negative stat is removed. expect False
print("T5:", kept(raw, "Negative Stat Player"))

# checks if a player on exactly the minimum minutes is kept. expect True
print("T6:", kept(changed("Poacher A", "minutes_played", 450), "Poacher A"))

# checks if a player one minute below the minimum is removed. expect False
print("T7:", kept(changed("Poacher A", "minutes_played", 449), "Poacher A"))

# checks if a stat of exactly 0 is valid and kept. expect True
print("T8:", kept(changed("Poacher A", "goals_p90", 0), "Poacher A"))

# checks if an impossible percentage (140%) is removed. expect False
print("T9:", kept(changed("Playmaker A", "pass_completion_pct", 140), "Playmaker A"))

# checks if exactly 100% is valid and kept. expect True
print("T10:", kept(changed("Playmaker A", "pass_completion_pct", 100), "Playmaker A"))
