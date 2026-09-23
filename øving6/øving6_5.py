import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("soldata.csv", skiprows=8) #Må hoppe over første radene med info som forvirrer pandas
df["time"] = pd.to_datetime(df["time"], format="%Y%m%d:%H%M", utc=True, errors="coerce")
df = df.dropna(subset=["time"]) #Fjerner rader med ugyldig tid
df=df.set_index("time")
df = df.sort_index()

df["G(i)"] = pd.to_numeric(df["G(i)"])

juni_data = df.loc["2023-06-05"]

t = np.arange(0, 24, 1)

plt.plot(t, juni_data["G(i)"])
plt.xlabel("Tid")
plt.ylabel("Innstråling")
plt.grid()
plt.xticks(np.arange(0, 25, 1))
plt.show()

print(juni_data["G(i)"].dtype)
