import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv (r'C:\Users\Ron\Desktop\Sales_Time.csv')
df2 = pd.read_csv (r'C:\Users\Ron\Desktop\Sales_Time2.csv')

plt.hist(df, bins=20, alpha=0.4, normed=True)
#plot your other histogram here
plt.hist(df2, bins=20, alpha=0.4, normed=True)
plt.show()
