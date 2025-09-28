import pandas as pd

df = pd.read_csv("production_log.csv")

df.columns = df.columns.str.lower()

print("=== First 5 rows ===")
print(df.head())

df["timestamp"] = pd.to_datetime(df["timestamp"])

print("\n=== Data Info ===")
print(df.info())

print("\n=== Total number of events ===")
print(len(df))

df["date"] = df["timestamp"].dt.date
events_per_day = df.groupby("date")["event"].count()

print("\n=== Events per day ===")
print(events_per_day)

print("\n=== Most common events ===")
print(df["event"].value_counts())