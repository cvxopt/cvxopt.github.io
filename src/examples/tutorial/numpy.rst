Numpy and CVXOPT
""""""""""""""""

In Python 2.7, Numpy arrays and CVXOPT matrices are compatible and exchange 
information using the Array Interface.

A Numpy array is created from a matrix using Numpy's :func:`array` method.

>>> from cvxopt import matrix
>>> from numpy import array
>>> A = matrix([[1,2,3],[4,5,6]])
>>> print(A)
[ 1  4]
[ 2  5]
[ 3  6]
>>> B = array(A)
>>> B
array([[1, 4],
       [2, 5],
       [3, 6]])
>>> type(B)
<type 'numpy.ndarray'>

A CVXOPT matrix can be created from a Numpy array as follows.

>>> C = matrix(B)
>>> type(C)
<type 'cvxopt.base.matrix'>
