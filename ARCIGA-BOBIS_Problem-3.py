import numpy as np

in_int = [int(in_str) for in_str in input('Enter the data points (x, y) in succeeding order.\n '
                                          'Ex. 1 1 3 5: \n').split()]
n = int(len(in_int)/2)
data = np.zeros((n, 2), dtype=int)

for i in range(0, n):
    data[i][0] = in_int[i*2]
    data[i][1] = in_int[i*2+1]

x = data[:, 0]
y = data[:, -1]
errors = np.zeros(10)
for i in range(0, 10):
    if i == 10:
        break
    coefficients = np.polyfit(x, y, i+1)
    fxi = np.polyval(coefficients, x)
    ex = y - fxi
    error_vector = np.linalg.norm(ex)
    errors[i] = error_vector

index = np.argmin(errors)
coefficients = np.polyfit(x, y, index)
print('The degree of the function is: ', index)
print('The coefficients of the fit are:\n', coefficients)