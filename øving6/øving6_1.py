import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 500)

A = 800 
mu = 13
sigma = 3

G = A * np.exp(-(t - mu)**2 / (2 * sigma**2))

plt.plot(t, G)
plt.xlabel("Tid i timer")
plt.ylabel("Innstråling [W/m^2]")
plt.title("Døgnprofil for innstråling")
plt.xticks(np.arange(0, 25, 1))
plt.grid()
plt.show()
