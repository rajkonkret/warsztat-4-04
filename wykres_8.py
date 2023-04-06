import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
# for std in range(1, 4):
#     x = np.random.normal(0, std, 100)
#     data.append(x)
labels = ['Grupa 1', 'Grupa 2', 'Grupa 3']

plt.boxplot(data, labels=labels, showmeans=True)

outliers = [y for x in data for y in x if y < -2.5 or y > 2.5]
plt.plot(np.ones(len(outliers)), outliers, 'ro', alpha=0.5)
plt.title("Wykres pudełkowy")
plt.xlabel("Grupy")
plt.ylabel('Wartości')

plt.show()