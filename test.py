from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.sublopts()
ax.plot(x, y)
ax.set_title('Test')
arr = [-3, 1, 2, -2, 3, -1] 
plt.plot(arr)
plt.ylabel('fuck this shit')

substracted = [2 - i for i in arr]

plt.show()