import numpy as np
import scipy.linalg as linalg

print()


# a:
A = np.array([[1, -2, 3],
              [4, 5, 6,],
              [7, 1, 9,]])

# b:
b = np.array([1, 2, 3])

# c:
x = linalg.solve(A,b)

# d:
print(np.matmul(A,x))

# c:
B = np.random.random(9).reshape(3,3)
X = linalg.solve(A,B)

print(np.matmul(A,X), "\n = \n", B)


# d:
eigenvalues, eigenvectors = linalg.eig(A)
print(eigenvalues)
print(eigenvectors)

# e:
A_inv = linalg.inv(A)
A_det = linalg.det(A)
print(A_inv)
print(A_det)

# f:
norm_1 = linalg.norm(A,ord=1)
norm_2 = linalg.norm(A,ord=2)
print(norm_1,norm_2)