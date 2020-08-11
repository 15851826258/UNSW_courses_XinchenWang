## import modules here
import pandas as pd
import numpy as np


################# Question 1 #################

def cal_sse(L):  # To calculate the sse
    if (len(L) < 0):  # if there is no ele in the bin
        return -1
    variance = np.var(L)
    result = variance * len(L)
    if result==0.0:
        result=0
    # print(result)
    return result



def v_opt_dp(x, b):  # do not change the heading of the function
    # create the matrix
    L_matrix = [[0 for i in range(len(x))] for j in range(b)]  # matrix for output
    L_bin = [[0 for i in range(len(x))] for j in range(b)]  # matrix for the bin
    L_sum_index = [[0 for i in range(len(x))] for j in range(b)]  # matrix for sse s
    for i in range(b):
        for j in range(len(x) - 1, -1, -1):
            if (j < b - i -1):
                L_matrix[i][j] = -1
            elif (j >= len(x)-i ):
                L_matrix[i][j] = -1
            else:
                L_matrix[i][j] = 100# mark the value that should be calculated


    for i in range(len(x) - 1, -1, -1):
        if (L_matrix[0][i] == 100):
            # print(x[i:])
            # L_matrix[0][i]=3
            L_matrix[0][i] = cal_sse(x[i:])
            L_bin[0][i] = x[i:]

    for i in range(1, b):
        for j in range(len(x) - 1, -1, -1):
            if (L_matrix[i][j] == 100):  # use the mark to identify the num that need change
                L_sse = []  # create a list to put result of see
                L_curr = []
                for k in range(j+1, len(x)):
                    last_result = L_matrix[i - 1][k]
                    if last_result != -1:
                        current_sse = cal_sse(x[j:k])
                        sse = current_sse + last_result
                        L_curr.append(current_sse)
                        L_sse.append(sse)
                        #print(x[j:k])
                min_index = L_sse.index(min(L_sse))
                #current_sse = L_curr[min_index]
                # print("min_index is",min_index,L_sse[min_index])
                # print(x[j:j+1+min_index])
                L_matrix[i][j] = min(L_sse)  # put the min sse to the matrix
                L_bin[i][j] = x[j:j + 1 + min_index]
                # print("\n")
                # print(min(L_sse))
                L_sum_index[i][j] = min_index + j
    # for row in L_bin:
    #     print(row)
    # print('\n')
    L_output = []
    start_index = 0
    L_output.append(L_bin[-1][0])  # the first ele in result
    for i in range(0, b - 1):
        start_index = L_sum_index[b - i - 1][start_index] + 1
        L_output.append(L_bin[b - i - 1 - 1][start_index])
        # print(b-i-1,start_index)
    # for row in L_bin:
    #     print(row)
    return L_matrix, L_output


# You can test your implementation using the following code...
x = [3, 1, 18, 11, 13,17]
num_bins = 4
x = [7,9,13,5]
num_bins = 3
v_opt_dp(x, num_bins)
matrix, bins = v_opt_dp(x, num_bins)
print("Bins = {}".format(bins))
print("Matrix =")
for row in matrix:
    print(row)
