import numpy as np
arr1 = np.array([[2,4], [4, 5]])
print("\nDeterminant of matrix:")
print(np.linalg.det(arr1))
print("\nInverse of matrix:")
print(np.linalg.inv(arr1))
print("\nRank of matrix:")
print(np.linalg.matrix_rank(arr1))
print("\nTransform matrix into 1-D array:")
print(np.reshape(arr1,-1))


output
mlm@mlm-desktop:~$ python3 square.py

Determinant of matrix:
-6.0

Inverse of matrix:
[[-0.83333333  0.66666667]
 [ 0.66666667 -0.33333333]]

Rank of matrix:
2

Transform matrix into 1-D array:
[2 4 4 5]
mlm@mlm-desktop:~$ 




