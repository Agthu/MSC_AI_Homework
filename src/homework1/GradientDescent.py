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


'''

共迭代1374次，输出结果:

x0:  [1, 1]
grad  [4, 2]
----------epoch 1 ----------
norm  4.47213595499958
x  [0.96, 0.98]
grad  [3.84, 1.96]
----------epoch 2 ----------
norm  4.3112875107095325
x  [0.923136, 0.960792]
grad  [3.692544, 1.921584]
----------epoch 3 ----------
norm  4.162615315038371
x  [0.8890487970201599, 0.94232957465472]
grad  [3.5561951880806397, 1.88465914930944]
...
...
...
----------epoch 1374 ----------
norm  0.10001177335772299
x  [0.017818353225446934, 0.03502967216587307]
grad  [0.07127341290178774, 0.07005934433174614]

'''