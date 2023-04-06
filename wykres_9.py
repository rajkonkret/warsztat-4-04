import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 3, 101)
y = np.linspace(-3, 3, 101)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X-1)**2 - Y**2)
Z3 = np.exp(-(X+1)**2 - Y**2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z1, cmap='Reds')
ax.plot_surface(X, Y, Z2, cmap='Blues')
ax.plot_surface(X, Y, Z3, cmap='Greens')

ax.set_xlabel('Os X')
ax.set_ylabel('Os Y')
ax.set_zlabel('Os Z')

ax.set_title('Wykres powierzchniowy')

plt.show()
# 11:30