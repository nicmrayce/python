import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv (r'C:\Users\Ron\Desktop\Sales_Time.csv')
print (df)

plt.hist(df, bins=20)
plt.show()
