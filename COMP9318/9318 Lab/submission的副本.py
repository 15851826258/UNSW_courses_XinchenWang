import pandas as pd
import numpy as np

def sigmoid(x):  # use the sigmoid function to calculate the result between 0 adn 1
    s = -1 * (1 / (1 + np.exp(-x)))  # get the difference for the calculate
    s = np.array(s)
    return s


def logistic_regression(data, labels, weights, num_epochs, learning_rate):
    size = data.shape[0]  # get the data size
    data = np.insert(data, 0, np.ones(size), axis=-1)
    data = np.mat(data)  # change the data to a matrix
    matrix_label=np.mat(labels)
    label_trans=matrix_label.T
    for i in range(0, num_epochs):
        z_matrix = np.multiply(data, weights)  # calculate as z=ax+by+c
        sum_z_matrix = z_matrix.sum(axis=1)  # calculate sum in horizontal way to get z
        log = sigmoid(sum_z_matrix)
        comb_matrix = np.hstack((log, label_trans))
        sum_combo_matrix = comb_matrix.sum(axis=1)  # calculate the erro each time
        dif_matrix = np.multiply(sum_combo_matrix, data)
        dif_learning_rate = learning_rate * dif_matrix.sum(axis=0)# get the learning rate
        weights=weights+dif_learning_rate
    weights_list=weights.tolist()#tranfer to list and return the first value
    return weights_list[0]
