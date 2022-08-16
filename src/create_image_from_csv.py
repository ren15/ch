import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mem_info.csv")

print(df)

plt.plot(df)
plt.savefig('mem_info.png')
