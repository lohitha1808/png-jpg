import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.figure(figsize=(8, 4))
plt.plot(df['Date'], df['Sales'], marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()

plt.savefig('sales_chart.png')
print("Chart saved as sales_chart.png")
