import matplotlib.pyplot as plt
import numpy as np

arr = []
for i in range(1, 101, 23):
    arr.append(i)
    
x = np.array(arr)

plt.pie(x)
plt.show()