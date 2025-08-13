import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20250808',periods=6)
print(dates)

#np.random.randn生成 标准正态分布（均值为 0，方差为 1）的随机数（浮点数）
df = pd.DataFrame(np.random.randn(6,4),index=dates, columns=['a', 'b', 'c', 'd'])
print(df)


#一种方法，自己填入数据
df1 = pd.DataFrame(np.arange(12).reshape(3,4)) #行列标签他自己会补充
print(df1)

#第二种方法，字典的方式
df2 = pd.DataFrame({
  'A':1.,
  'B':pd.Timestamp(20250808),
  'C':pd.Series(1,index=list(range(4)),dtype=np.int32),
  'D':np.array([3]*4, dtype='int32'),
  'E':pd.Categorical(["test", "train", "test", "train"]),
  'F':'foo'
})# 每一列的数据
print(df2)

print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)#输出每一行的值
print(df2.describe())#输出每一行的count mean min

print(df2.sort_index(axis=1, ascending=False)) #对列的名称进行排序，flase代表倒序（从大到小）
print(df2.sort_index(axis=0, ascending=False)) #对行的名称进行排序，flase代表倒序（从大到小）

print(df2.T)

print(df2.sort_values(by='E'))