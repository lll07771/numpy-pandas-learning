import numpy as np

A = np.arange(3,15)
print(A)
print(A[3])

B = np.arange(3,15).reshape((3,4))
print(B)
print(B[2])
print(B[2][1])
print(B[2][0:2])

print(B)
print(B[1,2])
print(B[:,2])
print(B[1,:])

for row in B:
  print(row)

for col in B.T:
  print(col)

print(B.flatten())
for item in B.flat:
  print(item)