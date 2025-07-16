import pandas as pd

df = pd.read_csv("C:/Users/İREM/Desktop/biyoinformatik/second/sequences_st")
print(df.head())


import matplotlib.pyplot as plt

plt.hist(df["GC_Content"], bins=10, color='skyblue', edgecolor='black')
plt.title("GC İçeriği Dağılımı")
plt.xlabel("GC İçeriği (%)")
plt.ylabel("Sekans Sayısı")
plt.grid(True)
plt.tight_layout()
plt.show()
