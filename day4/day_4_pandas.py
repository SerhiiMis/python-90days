import pandas as pd


defect_log = [
    {"timestamp": "2025-10-23 09:00", "station": 5, "defect_type": "Weld Crack", "severity": "High"},
    {"timestamp": "2025-10-23 09:15", "station": 3, "defect_type": "Paint Scratch", "severity": "Low"},
    {"timestamp": "2025-10-23 09:30", "station": 5, "defect_type": "Misaligned Bolt", "severity": "Medium"},
    {"timestamp": "2025-10-23 09:45", "station": 7, "defect_type": "Weld Crack", "severity": "High"},
    {"timestamp": "2025-10-23 10:00", "station": 3, "defect_type": "Dust Inclusion", "severity": "Low"},
    {"timestamp": "2025-10-23 10:15", "station": 6, "defect_type": "Paint Scratch", "severity": "Medium"},
    {"timestamp": "2025-10-23 10:30", "station": 5, "defect_type": "Misaligned Bolt", "severity": "High"},
    {"timestamp": "2025-10-23 10:45", "station": 7, "defect_type": "Weld Crack", "severity": "High"},
    {"timestamp": "2025-10-23 11:00", "station": 4, "defect_type": "Dust Inclusion", "severity": "Low"},
    {"timestamp": "2025-10-23 11:15", "station": 6, "defect_type": "Paint Scratch", "severity": "Medium"}
]


df_defects = pd.DataFrame(defect_log)


print("--- Initial DataFrame (First 5 Rows) ---")
print(df_defects.head())
print("\n--- DataFrame Information ---")
print(df_defects.info())

defect_types = df_defects['defect_type']
print("\n--- Only Defect Types ---")
print(defect_types)

key_metrics = df_defects[['timestamp', 'station', 'severity']]
print("\n--- Key Metrics (Timestamp, Station, Severity) ---")
print(key_metrics)

high_severity_filter = df_defects['severity'] == 'High'

df_high_severity = df_defects[high_severity_filter]
print("\n--- Only High Severity Defects (Weld Cracks) ---")
print(df_high_severity)

df_critical_area = df_defects[
    (df_defects['severity'] == 'High') & (df_defects['station'] == 5)
]
print("\n--- Critical Area Defects (High Severity at Station 5) ---")
print(df_critical_area)