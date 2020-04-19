import numpy as np


# x1偏导
def f_x1(x1):
    return 4*x1


# x2偏导
def f_x2(x2):
    return 2*x2


# 起始点
x = [1, 1]
# 学习率
learningRate = 0.01
# 精度
accuracy = 0.1

grad = [4, 2]
norm = np.linalg.norm(grad)

print('x0: ', x)
print('grad ', grad)

i = 1
while True:

    x[0] = x[0] - learningRate*x[0]*grad[0]
    x[1] = x[1] - learningRate*x[1]*grad[1]
    grad[0] = f_x1(x[0])
    grad[1] = f_x2(x[1])
    print('----------epoch', str(i), '----------')
    print('norm ', norm)
    print('x ', x)
    print('grad ', grad)
    i += 1
    norm = np.linalg.norm(grad)
    if norm < accuracy:
        break

