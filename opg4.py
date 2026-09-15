import pandas as pd
df = pd.read_csv("load_data.csv", parse_dates=["Time(Local)"], decimal=",", index_col="Time(Local)")

df["Netto"] = (df["Production"] - df["Consumption"])

max_production = df["Production"].max()
min_production = df["Production"].min()
mean_production = df["Production"].mean()

print(max_production, min_production, mean_production)
