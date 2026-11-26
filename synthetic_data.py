import pandas as pd

players = [
    # the attackers section of the synthetic database
    {"name": "Poacher A", "position_group": "ST", "age": 27, "minutes_played": 2400, "market_value": 40_000_000,
     "npxg_p90": 0.65, "shots_p90": 4.2, "touches_box_p90": 6.5, "goals_p90": 0.70, "sca_p90": 1.5},
    {"name": "Poacher B", "position_group": "ST", "age": 24, "minutes_played": 2100, "market_value": 15_000_000,
     "npxg_p90": 0.60, "shots_p90": 4.0, "touches_box_p90": 6.2, "goals_p90": 0.65, "sca_p90": 1.4},
    {"name": "Poacher C", "position_group": "ST", "age": 29, "minutes_played": 2600, "market_value": 55_000_000,
     "npxg_p90": 0.68, "shots_p90": 4.4, "touches_box_p90": 6.8, "goals_p90": 0.72, "sca_p90": 1.6},
    {"name": "Creator A", "position_group": "ST", "age": 26, "minutes_played": 2300, "market_value": 35_000_000,
     "npxg_p90": 0.30, "shots_p90": 2.1, "touches_box_p90": 3.0, "goals_p90": 0.28, "sca_p90": 4.5},
    {"name": "Creator B", "position_group": "ST", "age": 23, "minutes_played": 1900, "market_value": 12_000_000,
     "npxg_p90": 0.28, "shots_p90": 2.0, "touches_box_p90": 2.8, "goals_p90": 0.25, "sca_p90": 4.2},
    {"name": "Creator C", "position_group": "ST", "age": 31, "minutes_played": 2500, "market_value": 20_000_000,
     "npxg_p90": 0.32, "shots_p90": 2.2, "touches_box_p90": 3.1, "goals_p90": 0.30, "sca_p90": 4.7},

     #coding the midfield part of the synthetic database
      {"name": "Playmaker A", "position_group": "CM", "age": 28, "minutes_played": 2700, "market_value": 45_000_000,
     "prog_passes_p90": 8.5, "passes_final_third_p90": 6.0, "tackles_int_p90": 1.5, "pass_completion_pct": 90.0, "touches_p90": 85.0},
    {"name": "Playmaker B", "position_group": "CM", "age": 25, "minutes_played": 2400, "market_value": 18_000_000,
     "prog_passes_p90": 8.0, "passes_final_third_p90": 5.7, "tackles_int_p90": 1.4, "pass_completion_pct": 89.5, "touches_p90": 82.0},
    {"name": "Playmaker C", "position_group": "CM", "age": 30, "minutes_played": 2600, "market_value": 30_000_000,
     "prog_passes_p90": 8.8, "passes_final_third_p90": 6.3, "tackles_int_p90": 1.6, "pass_completion_pct": 91.0, "touches_p90": 87.0},
    {"name": "Destroyer A", "position_group": "CM", "age": 27, "minutes_played": 2500, "market_value": 25_000_000,
     "prog_passes_p90": 3.0, "passes_final_third_p90": 1.8, "tackles_int_p90": 6.5, "pass_completion_pct": 82.0, "touches_p90": 55.0},
    {"name": "Destroyer B", "position_group": "CM", "age": 24, "minutes_played": 2200, "market_value": 10_000_000,
     "prog_passes_p90": 2.8, "passes_final_third_p90": 1.6, "tackles_int_p90": 6.2, "pass_completion_pct": 81.0, "touches_p90": 52.0},
    {"name": "Destroyer C", "position_group": "CM", "age": 29, "minutes_played": 2600, "market_value": 15_000_000,
     "prog_passes_p90": 3.2, "passes_final_third_p90": 2.0, "tackles_int_p90": 6.8, "pass_completion_pct": 83.0, "touches_p90": 58.0},


]