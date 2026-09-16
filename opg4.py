import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("load_data.csv", parse_dates=["Time(Local)"], decimal=",")
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z", utc=True)
df=df.set_index("Time(Local)")
df = df.sort_index()
df["Netto"] = (df["Production"] - df["Consumption"])

#dogn = df.loc["2026-01-01"]
#dogn.plot()
#plt.xlabel("Tid")
#plt.ylabel("Effekt")
#plt.grid()
#plt.show()

max_production = df["Production"].max()
min_production = df["Production"].min()
mean_production = df["Production"].mean()

max_netto = df["Netto"].max()
min_netto = df["Netto"].min()

idx_max_netto = df["Netto"].idxmax()
idx_min_netto = df["Netto"].idxmin()

#print(max_netto, idx_max_netto)
#print(min_netto, idx_min_netto)

sum_production = df["Production"].sum()

df.plot(y=["Production", "Consumption", "Netto"], figsize=(10, 5))
plt.xlabel("Tid")
plt.ylabel("Effekt")
plt.title("Produksjon og forbruk over tid")
plt.grid()
plt.show()
