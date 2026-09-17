import math
import numpy as np
import matplotlib.pyplot as plt

l0 = 1
Ai = 1
t = np.linspace(0, 100, 101)
myi = 25
sigmai = 30

l_t = l0 + Ai*np.exp(-(t - myi)**2 /(2*sigmai**2))

plt.plot(t, l_t)
plt.grid()
plt.show()
