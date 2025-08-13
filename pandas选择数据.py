import numpy as np
import pandas as pd

dates = pd.date_range('20250809',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
print(df)

# print(df['A'], df.A,sep='\n')
# print(df[0:1], df['20250809':'20250811'], sep='\n')

# select by label:loc
print(df.loc['20250810'])
print(df.loc[:, ['A', 'B']])
print(df.loc['20250810', ['A', 'B']])

# select by position:iloc 像np里的索引一样筛选
print(df.iloc[[1,3,5], 1:3])

# Boolean indexing 
print(df[df.A > 8])