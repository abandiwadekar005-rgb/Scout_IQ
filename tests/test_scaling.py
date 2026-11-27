import pandas as pd
from database import PlayerDatabase
from preprocessing import clean_players, scale_by_position, STAT_COLUMNS

cleaned = clean_players(PlayerDatabase().get_all_players())
scaled = scale_by_position(cleaned)

# checks if every scaled column has a mean of about 0. expect True
print("T1:", all(abs(scaled[p][0][c].mean()) < 1e-9 for p in scaled for c in STAT_COLUMNS[p]))

# checks if every scaled column has a standard deviation of about 1. expect True
print("T2:", all(abs(scaled[p][0][c].std(ddof=0) - 1) < 1e-9 for p in scaled for c in STAT_COLUMNS[p]))

# checks if player_id is kept in the same order as the input. expect True
print("T3:", all(list(scaled[p][0]["player_id"]) ==
                 list(cleaned[cleaned["position_group"] == p]["player_id"]) for p in scaled))

# checks if a position with no players is skipped without crashing. expect ['CM', 'CB']
no_strikers = cleaned[cleaned["position_group"] != "ST"]
print("T4:", list(scale_by_position(no_strikers).keys()))

# checks if a stat where every player has the same value is handled without crashing. expect [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
same_value = cleaned.copy()
same_value.loc[same_value["position_group"] == "ST", "goals_p90"] = 0.5
print("T5:", list(scale_by_position(same_value)["ST"][0]["goals_p90"]))
