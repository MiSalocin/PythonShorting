import time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dt = 0


def insertionSort(array):
    t0 = time.perf_counter()
    global dt
    for x in range(len(array)):
        while array[x] < array[x - 1] and x > 0:
            temp = array[x]
            array[x] = array[x - 1]
            array[x - 1] = temp
            x = x - 1
    dt = time.perf_counter() - t0
    print(time.perf_counter())


plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 16

N = int(input("How many number do you wanna randomize?"))
arr = np.round(1000 * np.random.random_sample(N), 0)

fig, ax = plt.subplots()
ax.bar(range(0, len(arr)), arr, align="edge")

insertionSort(arr)
print(f"Array shorted in {dt*1E3:.3f} ms")

fig, ax = plt.subplots()
ax.bar(range(0, len(arr)), arr, align="edge")
plt.show()
