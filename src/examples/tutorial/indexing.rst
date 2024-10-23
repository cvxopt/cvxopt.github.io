Indexing of matrices
""""""""""""""""""""

There are two approaches for indexing dense and sparse matrices: 
single-argument indexing and double-argument indexing.
In double-argument indexing a matrix is indexed using two index-sets 
`I` and `J`.

>>> from cvxopt import matrix
>>> A = matrix(range(16),(4,4))
>>> print(A)
[  0   4   8  12]
[  1   5   9  13]
[  2   6  10  14]
[  3   7  11  15]
>>> print(A[[0,1,2,3],[0,2]])
[  0   8]
[  1   9]
[  2  10]
[  3  11]

The index-sets can be integers, lists, integer matrices, or slices.

>>> print(A[1,:])
[  1   5   9  13]
>>> print(A[::-1,::-1])
[ 15  11   7   3]
[ 14  10   6   2]
[ 13   9   5   1]
[ 12   8   4   0]

In single-argument indexing a matrix is indexed in vector-form by 
considering the matrix in column-major order (i.e., by stacking the 
columns from left to right).

>>> A[::5] = -1
>>> print(A)
[ -1   4   8  12]
[  1  -1   9  13]
[  2   6  -1  14]
[  3   7  11  -1]

This is useful for accessing parts of matrix that are not sub-matrices, 
e.g., the diagonal part of a matrix.
