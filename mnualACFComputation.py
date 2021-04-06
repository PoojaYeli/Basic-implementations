import matrixprofile as mp
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import argrelmax
from statsmodels.graphics.tsaplots import plot_acf

def comp_acf(y, lag=150):
    x = y
    lag_l = 0
    norm = 0
    res_acf = []
    while lag_l <= lag:
        y_cpy = y[lag_l:len(y)]
        x_cpy = x[0:len(x)-lag_l]
        y_mean = np.mean(y_cpy)
        x_mean = np.mean(x_cpy)
        # sub_y = [i - np.mean(y_cpy) for i in y_cpy]
        # sub_x = [i - np.mean(x_cpy) for i in x_cpy]
        # numerator = sum([sub_x[i] * sub_y[i] for i in range(len(sub_x))])
        # print("numerator:", numerator)
        sub_y = y_cpy - y_mean
        sub_x = x_cpy - x_mean
        cov = sum(sub_y * sub_x)
        # print("num:", cov)
        if lag_l == 0:
            norm = cov
        # print("num:", numerator/norm)
        res_acf.append(cov / norm)
        lag_l = lag_l + 1
    return res_acf

# Load Data
input_file = '/home/file_name.txt'
f = open(input_file, 'r')
lines = f.readlines()
dataset = []
for line in lines:
    dataset.append(float(line))

res = comp_acf(dataset, 500)
res = np.array(res)
# print(res)
# find size of period- local maxima
# x[argrelextrema(x, np.greater)[0]]
local_maxima = argrelmax(res)[0]
#select the positive peaks only
window_size = local_maxima[res[local_maxima] > 0]
print(window_size)
plt.bar(np.arange(len(res)),res)
plt.show()
