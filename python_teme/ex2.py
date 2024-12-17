import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('data.csv')

data.plot()
plt.title("Grafic 1")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend(title="Parametrii")
plt.show()

data2 = data[:4]
plt.plot(data2, marker='o')
plt.title("Grafic 2")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend(data2, title="Parametrii")
plt.show()

data3 = data[["Durata", "Puls"]][-10:]
plt.plot(data3, marker = "*")
plt.title("Grafic 3")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend(data3, title="Parametrii")
plt.show()

