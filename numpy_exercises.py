import numpy as np


# a:
vector = np.zeros(10)
vector[4] = 1
print(vector)

# b:
vector_range = np.arange(10,50)
print(vector_range)

# c:
vector_reversed = np.copy(vector_range[::-1])
print(vector_reversed)

# d:
matrix_range = np.arange(0,9)
matrix_range = np.reshape(matrix_range,[3,3])
print(matrix_range)

# e:
vector = np.array([1,2,0,0,4,0])
indicies = np.where(vector!=0)
print(indicies)

# f:
random_vector =np.random.random(30)
mean_value = np.mean(random_vector)
print(mean_value)

# g:
n_entries = 8
array_2D = np.zeros([n_entries,n_entries])
array_2D[:,0] = 1
array_2D[:,-1] = 1
array_2D[0,:] = 1
array_2D[-1,:] = 1
print(array_2D)

# h:
n_entries = 8
checkerboard = np.zeros([n_entries,n_entries])
checkerboard[::2,::2] = 1
checkerboard[1::2,1::2] = 1
print(checkerboard)
# import matplotlib.pyplot as plt
# plt.figure()
# plt.imshow(checkerboard)
# plt.show()

# i:
checkerboard_tile = np.array([[1,0],
                              [0,1]])
checkerboard = np.tile(checkerboard_tile,[4,4])
print(checkerboard)

# j:
array_1D = np.arange(11)
array_1D[(array_1D>=3) & (array_1D<=8)] = -array_1D[(array_1D>=3) & (array_1D<=8)] 
print(array_1D)

# k:
Z = np.random.random(10)
Z_sorted = np.sort(Z)
print(Z_sorted)

# l:
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = all(A == B)

# m:
Z = np.arange(10, dtype=np.int32)
print(Z.dtype, Z)
Z = Z.astype(np.float32)
print(Z.dtype, Z)

# n:
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(D)



# Advanced exercises:
# a:
coordinates = np.array([[1.0, 2.0, 10],
                        [3.0, 4.0, 20],
                        [5.0, 6.0, 30],
                        [7.0, 8.0, 40]])
coordinates_normalized = coordinates/coordinates[:,-1][:,np.newaxis]
print(coordinates_normalized)

# b:
size = 3
array_3x3 = np.random.random(int(size*size)).reshape(size,size)
diagonal = array_3x3[[range(size)],[range(size)]]
print(diagonal)

# c:
size_i = 10
size_j = 3
array_3x10 = np.random.random(int(size_i*size_j)).reshape(size_i,size_j)

closest_to_075 = array_3x10[np.argmin(abs(array_3x10-0.75),axis=1)]
print(closest_to_075)

# d:
x = np.empty((10, 8, 6))

idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

print("The shape must be equal to idx0, i.e. [3,8]")
print("Verification:",np.shape(x[idx0, idx1, idx2]))

# e:
x = np.arange(12, dtype=np.int32).reshape((3, 4))

z = np.lib.stride_tricks.as_strided(x, shape=(2, 3, 2, 2), strides=(16, 4, 16, 4))
print(z)