import math

import numpy as np


def f(x):
    return x * math.log(x) - 16.0


xvals = np.arange(0.01, 10, 0.01)
yvals = np.array([f(x) for x in xvals])


def fprime(x):
    return 1.0 + math.log(x)


def find_root(f, fprime, x_0=1.0, EPSILON=1E-7, MAX_ITER=1000):  # do not change the heading of the function
    x_NEW = x_0;
    x_OLD = x_0;
    time = 0
    while (time < MAX_ITER):#control the max times
        time += 1
        x_OLD = x_NEW #get the result of the previous loop
        x_NEW = x_NEW - f(x_NEW) / fprime(x_NEW) #use the formular
        if (abs(x_OLD - x_NEW) < EPSILON):# use EPSILON to control the loop
            return x_NEW
    return x_NEW
    pass  # **replace** this line with your code


x = find_root(f, fprime)
print(x)
print(f(x))
