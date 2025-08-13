import numpy as np
import pandas as pd

dates = pd.date_range('20250809', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print(df)
#把缺失值直接丢弃 dropna
print(df.dropna(axis=0, how='any')) #how = {'any', 'all'}

#把缺失值用其他数值代替
print(df.fillna(value=0))

print(df.isnull())

print(np.any(df.isnull()) == True)