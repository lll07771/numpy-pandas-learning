import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B)) # vertical stack 上下合并
print(A.shape, C.shape)

D = np.hstack((A,B)) # horizontal stack 左右合并
print(D)
print(D.shape)

print(A[np.newaxis, :].shape) #增加新行
print(A[np.newaxis, :])
print(A[:, np.newaxis].shape)
print(A[:, np.newaxis])

A = np.array([1,1,1])[:, np.newaxis]
B = np.array([2,2,2])[:, np.newaxis]
D = np.hstack((A, B))
print(D)

E = np.concatenate((A,B,B,A), axis=0)
F = np.concatenate((A,B,B,A), axis=1)
print("上下合并: ", E)
print("左右合并: ", F)