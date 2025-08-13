import numpy as np

#关联copy
A = np.arange(4)
B = A
C = A
D = B
print(A)
A[0] = 11
print(A)
print(B is A)
print(B, C)
print(D is A)
print(D)
D[1:3] = [22,33]
print(A, D)

#deep copy 有赋值,但不关联

a = np.arange(4)
b = np.copy(a)
a[3] = 44
print(a is b)
print(a, b)