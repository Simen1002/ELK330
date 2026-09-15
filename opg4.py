import pandas as pd
df = pd.read_csv("load_data.csv", parse_dates=["Time(Local)"], decimal=",", index_col="Time(Local)")

df["Netto"] = (df["Production"] - df["Consumption"])

print(df.head())
