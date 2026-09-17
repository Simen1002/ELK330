import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ProductionConsumption-2026.csv", parse_dates=["Time(Local)"])
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z", utc=True)
df=df.set_index("Time(Local)")
df = df.sort_index()

dogn = df.loc["2026-03-25", "Consumption"]

l0 = 1
Ai = 1
t = np.arange(24)
myi = 25
sigmai = 30

#l_t = l0 + Ai*np.exp(-(t - myi)**2 /(2*sigmai**2))

plt.plot(t, dogn.values, marker="o", linestyle="None")
plt.xlabel("Tid i timer")
plt.ylabel("Forbruk")
plt.grid()
plt.show()
