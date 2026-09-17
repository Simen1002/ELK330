import math
import numpy as np
import matplotlib as plt

l0 = 1
Ai = 1
t = np.linspace(0, 100, 101)
myi = 25
sigmai = 20

l_t = l0 + Ai*np.exp(-(t - myi)**2 /(2*sigmai**2))

plot(t, l_t)
