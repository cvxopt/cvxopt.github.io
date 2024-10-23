.. role:: raw-html(raw)
   :format: html

.. raw:: html

    <h1 style="letter-spacing: 0.6em; font-size: 2.5em !important;
    margin-bottom: 0; padding-bottom: 0"> CVXOPT </h1>
    <p style="color: #11557C; font-variant: small-caps; font-weight: bold;
    margin-bottom: 2em">
    Python Software for Convex Optimization </p>

.. title:: Home

CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main purpose
is to make the development of software for convex optimization applications
straightforward by building on Python's extensive standard library
and on the strengths of Python as a high-level programming language.


Current release
""""""""""""""""

Version 1.3 includes:

* efficient Python classes for dense and sparse matrices (real and complex),
  with Python indexing and slicing and overloaded operations for matrix
  arithmetic

* an interface to most of the double-precision real and complex BLAS

* an interface to LAPACK routines for solving linear equations and
  least-squares problems, matrix factorizations (LU, Cholesky,
  :raw-html:`LDL<sup><small>T</small></sup>` and QR),
  symmetric eigenvalue and singular value decomposition, and Schur
  factorization

* an interface to the fast Fourier transform routines from FFTW

* interfaces to the sparse LU and Cholesky solvers from UMFPACK and CHOLMOD

* routines for linear, second-order cone, and semidefinite programming
  problems

* routines for nonlinear convex optimization

* interfaces to the linear programming solver in GLPK, the semidefinite
  programming solver in DSDP5, and the linear, quadratic and second-order
  cone programming solvers in MOSEK

* a modeling tool for specifying convex piecewise-linear optimization
  problems.


Availability
""""""""""""""

A platform-independent source package is available from the Download
section, and pre-built packages are available via the Pip and Conda package managers
(refer to the installation instructions for further details).
CVXOPT can also be obtained from the Debian, Ubuntu, and Fedora
package repositories, and is included in
`Python(x,y) for Microsoft Windows <https://python-xy.github.io>`_.
Modeling interfaces to the CVXOPT solvers are available in
`CVXPY <http://cvxpy.org>`_ and `PICOS <http://picos.zib.de>`_.


Authors
"""""""""

CVXOPT is developed by Martin Andersen
(:raw-html:`<kbd>martin.skovgaard.andersen@gmail.com</kbd>`),
Joachim Dahl
(:raw-html:`<kbd>dahl.joachim@gmail.com</kbd>`),
and Lieven Vandenberghe
(:raw-html:`<kbd>vandenbe@ee.ucla.edu</kbd>`).

CVXOPT was originally developed for use in our own work, and is being made
available in the hope that it may be useful to others.
We welcome feedback, bug reports, and suggestions for improvements, but
can only offer very limited support.


.. toctree::
    :hidden:

    copyright
    download/index
    install/index
    documentation/index
    examples/index
    applications/index
