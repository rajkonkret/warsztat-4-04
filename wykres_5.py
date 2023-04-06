import matplotlib.pyplot as plt

labels = ['2016', '2017', '2018', '2019', '2020']
values = [10, 20, 30, 25, 35]

plt.bar(labels, values)
plt.title("Wykres słupkowy")
plt.xlabel('lata')
plt.ylabel('Wartości')
plt.show()
