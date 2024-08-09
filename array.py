import numpy as np
array_4x4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [12, 11, 10, 9],
    [15, 16, 17, 18]
])
print("Full array:")
print(array_4x4)
print()
print("Rows excluding the first:")
print(array_4x4[1:])
print()
print("Rows excluding the first and excluding the last column:")
print(array_4x4[1:, :-1])
print()
print("1st and 2nd columns in the 2nd and 3rd rows:")
print(array_4x4[1:3, 0:2])


output
mlm@mlm-OptiPlex-3020:~/Desktop$ python3 array123.py
Full array:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [12 11 10  9]
 [15 16 17 18]]

Rows excluding the first:
[[ 5  6  7  8]
 [12 11 10  9]
 [15 16 17 18]]

Rows excluding the first and excluding the last column:
[[ 5  6  7]
 [12 11 10]
 [15 16 17]]

1st and 2nd columns in the 2nd and 3rd rows:
[[ 5  6]
 [12 11]]
