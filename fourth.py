import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)

plt.figure(figsize=(15, 10))
ṇ
plt.subplot(2, 2, 1)
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Histogram')

plt.subplot(2, 2, 2)
sns.kdeplot(data, fill=True)
plt.title('Density Plot')

plt.subplot(2, 2, 3)
sns.boxplot(x=data)
plt.title('Box Plot')

plt.subplot(2, 2, 4)
sns.histplot(data, kde=True, bins=30, stat='density')
plt.title('Histogram with Density Plot')

plt.tight_layout()
plt.show()