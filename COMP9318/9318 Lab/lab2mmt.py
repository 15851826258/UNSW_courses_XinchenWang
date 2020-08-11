# These are the only modules that you can use in lab2
import pandas as pd
import numpy as np

x = [3, 1, 18, 11, 13, 17]
num_bins = 4

def SSE(L):
    mean = sum(L) / float(len(L))
    sse = 0
    for i in L:
        sse = sse + (i - mean ) ** 2
    if sse == 0.0:
        sse = 0
    return sse


def v_opt_dp(x, b):
    matrix = [[-1 for j in range(len(x))] for i in range(b)]
    matrix_path = [[-1 for j in range(len(x))] for i in range(b)]
    for i in  range(b):
        for j in range(len(x)-1,-1,-1):
            if j >= b - i-1 and j < len(x) - i:
                if i != 0:
                    opt = []
                    for n in range(j+1,len(x)):
                        if matrix[i-1][n] != -1:
                            opt.append(SSE(x[j:n]) + matrix[i-1][n])
                    matrix[i][j] = min(opt)
                    matrix_path[i][j] = opt.index(min(opt)) + j +1
                else:
                    matrix[i][j] = SSE(x[j:])
    index = 0
    Bin = []
    for i in range(b-1):
        pre_index = index
        index  =  matrix_path[b-i-1][index]
        Bin.append(x[pre_index:index])
        #print(index,pre_index)
    Bin.append(x[index:])
    # for row in matrix_path:
    #     print(row)

    return matrix, Bin


matrix, bins = v_opt_dp(x, num_bins)
print("Bins = {}".format(bins))
print("Matrix =")
for row in matrix:
    print(row)



