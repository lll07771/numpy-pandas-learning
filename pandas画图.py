import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plot data

#Series
# data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# data = data.cumsum()
# data.plot(title='Series Plot', figsize=(10, 6))
# plt.show()

# DataFrame
# data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD'))
# print(data.head(5))
# data = data.cumsum()
# print(data.head(5))
# data.plot(title='DataFrame Plot', figsize=(10, 6))
# plt.show()

#plot methods:
# line, bar, barh, hist, box, kde, area, scatter, hexbin, pie
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD'))
data = data.cumsum()
ax = data.plot(kind='scatter', x='A', y='B', title='Scatter Plot', figsize=(8, 6), color='blue', label='A vs B')
data.plot(kind='scatter', x='C', y='D', title='Scatter Plot', figsize=(8, 6), color='red', label='C vs D', ax=ax)
plt.legend()
plt.show()