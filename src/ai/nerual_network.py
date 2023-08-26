import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlabel("x1", fontsize=14)
ax.set_ylabel("x2", fontsize=14)
ax.set_aspect("equal", adjustable="box")

limit = 8
plt.xlim(-limit, limit)
plt.ylim(-limit / 2, limit)

y1 = x + 1
plt.plot(x, y1)

y2 = -x + 5
plt.plot(x, y2)

y3 = x
plt.plot(x, y3)

y4 = -x + 6
plt.plot(x, y4)

plt.axvline(x=5 / 2, ymin=-1.1, ymax=2.2)

plt.show()
