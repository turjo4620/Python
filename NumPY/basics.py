import numpy as np

# array representation

a = np.array([[1, 2, 3],
            [4, 5, 6]])
print(a)
print(a.shape)

# ndarray -> n dimensional array
# all the elements should be of one type
# and it must be rectangular, not jagged

b = np.array([1, 2, 3, 4])
b[0] = 100
print(b)

# colon notation [start : end + 1]
# prints start to end

print(b[: 3])

# Array attributes

# ndim -> number of dimensions

print(f"{a.ndim}  {b.ndim}")

# size -> number of elements 

print(a.size)

import math

print(a.size == math.prod(a.shape)) #True

# dtype -> returns the data type of the array

print(a.dtype)

# arrange -> first number, last number, and the step size

c = np.arange(2, 9, 2)
print(c)

