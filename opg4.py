import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("load_data.csv", parse_dates=["Time(Local)"], decimal=",")
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="mixed", utc = True)
df=df.set_index("Time(Local)")
df["Netto"] = (df["Production"] - df["Consumption"])

max_production = df["Production"].max()
min_production = df["Production"].min()
mean_production = df["Production"].mean()

max_netto = df["Netto"].max()
min_netto = df["Netto"].min()

dogn = df.loc["2026-01-01"]
dogn.plot()
plt.xlabel("Tid")
plt.ylabel("Effekt")
plt.grid()
plt.show()  