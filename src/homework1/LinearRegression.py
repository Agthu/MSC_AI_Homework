import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # 等差数列
# ar = np.linspace(0, 1, 11)
# print(ar)
# # 等比数列
# a = np.logspace(1, 2, 2)
# print(a)
# # 全0
# print(np.zeros(10, np.int))
# # 全1
# print(np.ones((9, 2), np.int))
# # 空
# print(np.empty((2, 3)))


# def func(i):
#     return i*2
#
#
# # 第一个参数为计算每个数组元素的函数，第二个参数为数组的大小(shape)
# a = np.fromfunction(func, (10, ))
# print(a)


# a = np.array([10, 9, 8, 7, 6, 5, 4])
# print(a)
# b = a[[1, 1, 6, 2]]
# print(b)


# # 结构数组
# persontype = np.dtype({
#     'names': ['name', 'age', 'weight'],
#     'formats': ['S32', 'i', 'f']
# })
#
# a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)], dtype=persontype)
# print(a)


# # 内置操作函数
# print(np.log(np.e))
# # >>>1.0

# --------------------------------------以上全是笔记--------------------------------------------

# x的平均数
def avg_x():
    return np.mean(data[:, :1])


# y的平均数
def avg_y():
    return np.mean(data[:, 1:])


# x的平方和
def sum_x2():
    s = [0]
    for i in data[:, :1]:
        s += i*i
    return s[0]


# xy求和
def sum_xy():
    s = 0
    for i, j in data:
        s += i*j
    return s


# 输入数据
data = np.array([(119, 230), (39, 143), (163, 384), (294, 314), (297, 616), (400, 1000),
                 (525, 763), (683, 774), (756, 1001), (981, 920), (1101, 1259), (1346, 1410)])
# 数据总数
n = 12
# 系数
w = (sum_xy() - n * avg_x() * avg_y()) / (sum_x2() - n * avg_x() * avg_x())
b = avg_y() - w * avg_x()


print(w)
