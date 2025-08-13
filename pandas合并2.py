import numpy as np
import pandas as pd

# left = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
#                      'A':['A0', 'A1', 'A2', 'A3'],
#                      'B':['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
#                       'C':['C0', 'C1', 'C2', 'C3'],
#                       'D':['D0', 'D1', 'D2', 'D3']})
# print(left,sep='\n')
# print(right)

# res = pd.merge(left, right, on='key') #默认是内连接 = 'inner',只考虑相同的key
# print(res)

# left = pd.DataFrame({'key1':['K0', 'K0', 'K1', 'K2'],
#                      'key2':['K0', 'K1', 'K0', 'K1'],
#                      'A':['A0', 'A1', 'A2', 'A3'],
#                      'B':['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1':['K0', 'K1', 'K1', 'K2'],
#                       'key2':['K0', 'K0', 'K0', 'K0'],
#                       'C':['C0', 'C1', 'C2', 'C3'],
#                       'D':['D0', 'D1', 'D2', 'D3']})

# # how = ['left', 'right', 'outer', 'inner']
# print(left, sep='\n')
# print(right, sep='\n')
# res = pd.merge(left, right, on=['key1', 'key2'], how='inner') 
# print(res)

#indicator
# df1 = pd.DataFrame({'col1':[0, 1], 'col_left':['A', 'B']})
# df2 = pd.DataFrame({'col1':[1,2,2], 'col_right':[2,2,2]})
# print(df1, sep='\n')
# print(df2, sep='\n')
# res = pd.merge(df1, df2, on='col1', how='outer', indicator=True) #indicator=True会添加一列'_merge'，显示合并的来源
# print(res)
# res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column') #可以自定义列名
# print(res)

# df1 = pd.DataFrame({'A':['A0', 'A1', 'A2'],
#                     'B':['B0', 'B1', 'B2']},
#                     index=['K0', 'K1', 'K2'])
# df2 = pd.DataFrame({'C':['C0', 'C2', 'C3'],
#                     'D':['D0', 'D2', 'D3']},
#                     index=['K0', 'K2', 'K3'])
# print(df1, sep='\n')
# print(df2, sep='\n')
#通过left_index和right_index指定通过索引合并
# res = pd.merge(df1, df2, left_index=True, right_index=True, how='outer') #通过索引合并
# print(res)

boys = pd.DataFrame({'key':['K0', 'K1', 'K2'],
                     'age':[1,2,3]})
girls = pd.DataFrame({'key':['K0', 'K0', 'K3'],
                      'age':[4,5,6]})
print(boys, sep='\n')
print(girls, sep='\n')
# suffix是用来区分同名列的,可以指定后缀,多用于两个DataFrame合并
# 两个DataFrame有相同列名时,可以指定后缀
res = pd.merge(boys, girls, on='key', suffixes=['_boy', '_girl'], how='outer') #通过索引合并how = ['left', 'right', 'outer', 'inner']
print(res)