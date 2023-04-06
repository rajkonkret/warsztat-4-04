import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.plot(x, y1, label="Sin")
plt.plot(x, y2, label="Cos")
plt.plot(x, y3, label="Tan")

plt.legend(title='Funkcja', loc='upper right')

plt.title('Wykres liniowy')
plt.xlabel('Oś x')
plt.ylabel('Oś y')

plt.show()