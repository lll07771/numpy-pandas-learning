import numpy as np

# //把一个列表转为矩阵的方法 np.array
array = np.array([[1,2,3],
                  [4,5,6]])
print(array) #输出array值
print("维数：",array.ndim)#输出维数
print("形状: ",array.shape)#输出形状
print("大小: ",array.size)#输出一共有多少元素

print(array.dtype)#int32

a = np.array([2,23,4], dtype = np.int64)
print(a.dtype)#int64
# 位数越小所占空间越小，位数越大所占空间越大但是越精准 np.float64

b = np.zeros(2)
print(b)
c = np.zeros((3,4))
print(c)
d = np.ones((3,4), dtype= np.int16)
print(d)

e = np.empty((3,4))#输出一个接近为零的数字
print(e)

f = np.arange(5) #输出一个有序序列 [0,5) 左闭右开  np.arange(start, end, step)
print(f)

g = np.arange(10, 22, 2).reshape((3,2)) #重新定义长和宽
print(g)

h = np.linspace(1, 10, 5) #(start, end, 多少段) 1到10有5段线段,自动分配
print(h)

i = np.linspace(1, 10, 6).reshape((2, 3))
print(i)