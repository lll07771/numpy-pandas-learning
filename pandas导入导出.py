import pandas as pd
import numpy as np
data = pd.read_csv('student.csv')
print(data)
print(data.shape)

data.iloc[0,0] = 1011
print(data)
data['grade'] = np.nan
print(data)
print(pd.isna(data))
print(data.fillna(value=100))
data['height'] = pd.Series(np.arange(160,188, 2), index=np.arange(14))
print(data)
data = data.fillna(value=100)
print(data)
data.to_pickle('student.pickle')