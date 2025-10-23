import pandas as pd


defect_log = [
    {"timestamp": "2025-10-23 09:00", "station": 5, "defect_type": "Weld Crack", "severity": "High"},
    {"timestamp": "2025-10-23 09:15", "station": 3, "defect_type": "Paint Scratch", "severity": "Low"},
    {"timestamp": "2025-10-23 09:30", "station": 5, "defect_type": "Misaligned Bolt", "severity": "Medium"},
    {"timestamp": "2025-10-23 09:45", "station": 7, "defect_type": "Weld Crack", "severity": "High"},
    {"timestamp": "2025-10-23 10:00", "station": 3, "defect_type": "Dust Inclusion", "severity": "Low"}
]


df_defects = pd.DataFrame(defect_log)


print("--- Initial DataFrame (First 5 Rows) ---")
print(df_defects.head())
print("\n--- DataFrame Information ---")
print(df_defects.info())