import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
c = a - b
print(c)

d = c**2
print(d)
e = 10*np.sin(a)
print(e)

print(e < 5)

f = np.array([[1,2],
              [3,4]])
g = np.arange(4).reshape((2,2))
print(f * g) #逐个相乘
print(np.dot(f, g))#矩阵相乘

h = np.random.random((2,4)) #随机生成一个size中范围0-1
print(h)

print(np.sum(f))
print(np.max(f))
print(np.min(f))

print(np.sum(f, axis= 1)) #axis = 1 在行求和
print(np.sum(f, axis= 0)) #axis = 0 在列求和

print(np.max(f, axis=1))

A = np.arange(2, 14).reshape((3,4))
print(np.argmin(A)) #输出矩阵最小值索引
print(np.argmax(A)) #输出矩阵最大值索引
print(np.mean(A)) #输出矩阵平均值
print(np.median(A)) #输出矩阵中位数
print(np.cumsum(A)) #逐个相加,前缀和
print(np.diff(A)) #后一个 - 前一个

B = np.array([[1,2,0,3],
             [2,3,4,0]])
print(np.nonzero(B)) 
print(np.sort(B))
print(B.T)
print((B.T).dot(B))

C = np.arange(14,2, -1).reshape((3,4))
print(C)
print(np.clip(C, 5, 9)) #矩阵中小于5的全部变成5,大于9的全部变成9
print(np.mean(C, axis= 0)) #列平均值
print(np.mean(C, axis= 1)) #行平均值