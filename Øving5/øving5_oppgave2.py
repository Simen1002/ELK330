import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ProductionConsumption-2026.csv", parse_dates=["Time(Local)"])
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z", utc=True)
df=df.set_index("Time(Local)")
df = df.sort_index()

#Utlavgt døgn
dogn = df.loc["2026-03-25", "Consumption"]

#Modellen
l0 = 15850

#Night peak
An = -350
myn = 2.5    #tid på topp
sigman = 1 #bredde
t = np.arange(24)

#Morning peak
Am = 2500
mym = 7
sigmam = 3

#Evening peak
Ae = 2500
mye = 19
sigmae = 4.5

night_peak =  An*np.exp(-(t - myn)**2 /(2*sigman**2))
morning_peak = Am*np.exp(-(t - mym)**2 /(2*sigmam**2))
evening_peak = Ae*np.exp(-(t - mye)**2 /(2*sigmae**2))

load_model = l0 + night_peak + morning_peak + evening_peak

#l_t = l0 + Ai*np.exp(-(t - myi)**2 /(2*sigmai**2))

plt.plot(t, dogn.values, marker="o", linestyle="None")
plt.plot(t, load_model)
plt.xlabel("Time")
plt.ylabel("Forbruk")
plt.xticks(np.arange(0, 24, 1))
plt.grid()
plt.show()