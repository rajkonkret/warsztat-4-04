import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

plt.plot(x, y)
plt.xlabel('Os X')
plt.ylabel('Os Y')
plt.title("Wykres")

plt.savefig('wykres.png', dpi=300, bbox_inches='tight')
plt.close()
