Creating matrices
"""""""""""""""""

CVXOPT has separate dense and sparse matrix objects.  This example 
illustrates different ways to create dense and sparse matrices.

A dense matrix is created using the :func:`matrix` function; 
it can be created from a list (or iterator):

>>> from cvxopt import matrix
>>> A = matrix([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], (2,3))
>>> print(A)
[ 1.00e+00  3.00e+00  5.00e+00]
[ 2.00e+00  4.00e+00  6.00e+00]
>>> A.size
(2, 3)

or from a list of lists, where each inner list represents a column of the 
matrix:

>>> B = matrix([ [1.0, 2.0], [3.0, 4.0] ])
>>> print(B)
[ 1.00e+00  3.00e+00]
[ 2.00e+00  4.00e+00]

More generally, the inner lists can represent block-columns.

>>> print(matrix([ [A] ,[B] ]))
[ 1.00e+00  3.00e+00  5.00e+00  1.00e+00  3.00e+00]
[ 2.00e+00  4.00e+00  6.00e+00  2.00e+00  4.00e+00]


The :func:`spmatrix` function creates a sparse matrix from a (value, row, 
column) triplet description.

>>> from cvxopt import spmatrix
>>> D = spmatrix([1., 2.], [0, 1], [0, 1], (4,2))
>>> print(D)
[ 1.00e+00     0    ]
[    0      2.00e+00]
[    0         0    ]
[    0         0    ]
>>> print(matrix(D))
[ 1.00e+00  0.00e+00]
[ 0.00e+00  2.00e+00]
[ 0.00e+00  0.00e+00]
[ 0.00e+00  0.00e+00]

Sparse matrices can also be constructed by concatenating other matrices 
using the :func:`sparse` function.

>>> from cvxopt import sparse
>>> E = sparse([ [B, B], [D] ])
>>> print(E)
[ 1.00e+00  3.00e+00  1.00e+00     0    ]
[ 2.00e+00  4.00e+00     0      2.00e+00]
[ 1.00e+00  3.00e+00     0         0    ]
[ 2.00e+00  4.00e+00     0         0    ]


Sparse block-diagonal matrices can be constructed using the :func:`spdiag` 
function.

>>> from cvxopt import spdiag
>>> print(spdiag([B, -B, 1, 2]))
[ 1.00e+00  3.00e+00     0         0         0         0    ]
[ 2.00e+00  4.00e+00     0         0         0         0    ]
[    0         0     -1.00e+00 -3.00e+00     0         0    ]
[    0         0     -2.00e+00 -4.00e+00     0         0    ]
[    0         0         0         0      1.00e+00     0    ]
[    0         0         0         0         0      2.00e+00]
