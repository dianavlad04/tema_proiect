import matplotlib.pyplot as plt
import pandas as pd 


df = pd.read_csv(r'C:\Users\Stefi Manda\Desktop\Python 2024\data.csv')


df.plot()
plt.title("Toate valorile")
plt.xlabel("Contor")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.grid()
plt.show()


df.head(5).plot()
plt.title("Primele 5 valori")
plt.xlabel("Contor")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.grid()
plt.show()


df[['Durata','Puls']].tail(17).plot()
plt.title("Ultimele 17 valori")
plt.xlabel("Contor")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.grid()
plt.show()
