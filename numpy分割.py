import numpy as np

A = np.arange(12).reshape((3,4))
print(A)

# print(np.split(A, 2, axis=1)) #对A的列分成两块
# print(np.split(A, 3, axis=0)) #对A的行分成三块
# print(np.array_split(A, 3, axis=1)) # array_split 可以进行不等块分割

print(np.vsplit(A,3))
print(np.hsplit(A,2))