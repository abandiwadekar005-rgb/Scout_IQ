from database import PlayerDatabase
from preprocessing import clean_players, scale_by_position, STAT_COLUMNS

cleaned = clean_players(PlayerDatabase().get_all_players())
cm = cleaned[cleaned["position_group"] == "CM"]
scaled_cm = scale_by_position(cleaned)["CM"][0]

# how much each stat varies between midfielders, before and after scaling
print("Spread of each CM stat (standard deviation):")
print(f"{'stat':<24}{'unscaled':>10}{'scaled':>10}")
for col in STAT_COLUMNS["CM"]:
    print(f"{col:<24}{cm[col].std(ddof=0):>10.2f}{scaled_cm[col].std(ddof=0):>10.2f}")