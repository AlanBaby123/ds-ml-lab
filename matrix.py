import numpy as np
array_1= np.array([
[1,2],
[5,6]])
array_2=np.array([[12,32],[55,86]])
print("matrix addition")
print(np.add(array_1,array_2))
print("matrix substarction")
print(np.subtract(array_1,array_2))
print("matrix division")
print(np.divide(array_1,array_2))
print("matrix multiplication")
print(np.multiply(array_1,array_2))
print("matrix multipication")
print(np.dot(array_1,array_2))
print("matrix Transpose")
print(array_1.transpose())
print("sum of digonal elements")
print(np.trace(array_1))




output
mlm@mlm-desktop:~$ python3 array4.py
matrix addition
[[13 34]
 [60 92]]
matrix substarction
[[-11 -30]
 [-50 -80]]
matrix division
[[0.08333333 0.0625    ]
 [0.09090909 0.06976744]]
matrix multiplication
[[ 12  64]
 [275 516]]
matrix multipication
[[122 204]
 [390 676]]
matrix Transpose
[[1 5]
 [2 6]]
sum of digonal elements
7
mlm@mlm-desktop:~$
