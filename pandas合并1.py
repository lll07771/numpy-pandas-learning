import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['A', 'B', 'C', 'D'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['A', 'B', 'C', 'D'])
print(df1, df2, df3)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True) #axis=0表示按行合并，axis=1表示按列合并
print(res)

# 以上都是默认 inner='outer'

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['A', 'B', 'C', 'D'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['B', 'C', 'D', 'E'], index=[2, 3, 4])
print(df1)
print(df2)

res = pd.concat([df1, df2])
print(res)

res = pd.concat([df1, df2], join='inner',ignore_index=True) #交集
print(res)

s1 = pd.Series([1,2,3,4],index=['A', 'B', 'C', 'D'])
# print(s1)
res = pd.concat([df1, s1.to_frame().T], join='outer', ignore_index=True) #Series和DataFrame合并
print(res)
