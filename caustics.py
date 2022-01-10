import numpy as np
import matplotlib as plt
s_list = [i for i in range(-5,5,0.1)]
t_list = [j for j in range(-5,5,0.1)]

x = t - s*np.exp(t) - 2*s
y = np.exp(t)

plt.plot(x,y)
