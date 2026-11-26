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

