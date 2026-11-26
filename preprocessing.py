import pandas as pd
from database import STAT_COLUMNS

# minimum minutes the player must play to process its data within the algorithm
MIN_MINUTES_THRESHOLD = 450

def clean_players(df):
    df = df.copy()
    df = df[df["minutes_played"] >= MIN_MINUTES_THRESHOLD]

    keep_mask = pd.Series(True, index=df.index)
    for position, cols in STAT_COLUMNS.items():
        pos_rows = df["position_group"] == position
        for col in cols:
            if col not in df.columns:
                continue
            null_here = pos_rows & df[col].isna()
            keep_mask &= ~null_here
            neg_here = pos_rows & (df[col] < 0)
            keep_mask &= ~neg_here

    return df[keep_mask].reset_index(drop=True)


if __name__ == "__main__":
    from database import get_all_players
    raw = get_all_players()
    cleaned = clean_players(raw)
    print(f"Raw: {len(raw)}, Cleaned: {len(cleaned)}")