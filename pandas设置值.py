import numpy as np
import pandas as pd

dates = pd.date_range('20250809', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])

df.iloc[2,2] = 111
df.loc['20250809', 'B'] = 222
print(df)

# df[df.A>4] = 0
# print(df)

# df.A[df.A>4] = 0
# print(df)

df.B[df.A>4] = 0
print(df)

df['F'] = np.nan
print(df)

df['E'] = pd.Series([1,2,3,4,5,6], index = pd.date_range('20250809',periods=6))
print(df)