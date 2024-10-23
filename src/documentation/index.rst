.. role:: raw-html(raw)
   :format: html

#############
Documentation
#############

User's guide
============

The
:raw-html:`<a href="../userguide/index.html">user's guide</a>`
distributed with the package is also available on-line.


Technical documentation
=======================

* The use of CVXOPT to develop customized interior-point solvers is decribed in the chapter
  `Interior-point methods for large-scale cone programming <http://www.seas.ucla.edu/~vandenbe/publications/mlbook.pdf>`_ (pdf), from the book
  *Optimization for Machine Learning* (edited by S. Sra, S. Nowozin, S. J. Wright, MIT Press, 2011).

* A discussion of the interior-point algorithms used in the
  :func:`conelp()` and :func:`coneqp()` solvers can be found in the
  report `The CVXOPT linear and quadratic cone program solvers
  <http://www.seas.ucla.edu/~vandenbe/publications/coneprog.pdf>`_ (pdf).


Discussion forum
================

There is a Google
`discussion forum <http://groups.google.com/forum/?fromgroups#!forum/cvxopt>`_ for  CVXOPT.


Revision history
================

**Version 1.3.2** (August 9, 2023).
    Bug fix 

**Version 1.3.1** (May 9, 2023).
    Minor improvements 

**Version 1.3.0** (March 8, 2022).
    Bug fixes and improved Python 3.11 compatibility. 

**Version 1.2.7** (September 20, 2021).
    Minor improvements and bug fixes. 

**Version 1.2.6** (February 18, 2021).
    Minor improvements and bug fix. 

**Version 1.2.5** (April 16, 2020).
    Python 3.8 and PyPy compatibility.

**Version 1.2.4** (January 20, 2020).
    Several bug fixes. Python 3.8 compatibility.

**Version 1.2.3** (February 5, 2019).
    Bug fix.

**Version 1.2.2** (October 18, 2018).
    Bug fix.

**Version 1.2.1** (August 30, 2018).
    Several bug fixes. 

**Version 1.2.0** (April 17, 2018).
    Several bug fixes. Improved Windows compatibility (Python 3.5+).

**Version 1.1.9** (November 30, 2016).
    Removed the SuiteSparse source code from the distribution.

**Version 1.1.8** (September 22, 2015).
    Upgrade to SuiteSparse version 4.4.5. Several bug fixes.

**Version 1.1.7** (May 31, 2014).
    Upgrades of the GLPK and MOSEK interfaces.

**Version 1.1.6** (April 22, 2013).
    Several bug fixes (int/int_t issues).  Performance improvements
    for certain spmatrix slicing operations.  Upgrade to SuiteSparse
    version 4.1.0.  Improved Numpy compatibility via buffer protocol
    (works in both Python 2.x and 3.x).  Improved SunOS/Solaris
    compatibility ("complex double" instead of "complex").

**Version 1.1.5** (March 28, 2012).
    Fixed a Mac OS X BLAS compatibility issue.

**Version 1.1.4** (December 21, 2011).
    Merged the source for the Python 2.7 and Python 3 versions.

**Version 1.1.3** (September 15, 2010).
    Upgrade of the MOSEK interface to MOSEK version 6.  A few bug fixes in
    the matrix class.

**Version 1.1.2** (December 15, 2009).
    Several bug fixes.  Improved initialization in the :func:`coneqp()`
    solver.

**Version 1.1.1** (March 1, 2009).
    Translated the user guide to Sphinx.  Additional LAPACK routines for
    LQ factorization and QR factorization with column pivoting.


**Version 1.1** (October 15, 2008).
    :func:`matrix()`, :func:`spmatrix()`, and the other functions in
    :mod:`cvxopt.base` can now be directly imported from cvxopt
    (":samp:`from cvxopt import matrix`" replaces
    ":samp:`from cvxopt.base import matrix`", although the older code still
    works).  `bool(A)` of a dense or sparse matrix `A` is now defined to be
    :const:`True` if `A` is a nonzero matrix. (Hence ":samp:`if A`" in older
    code should be replaced by ":samp:`if len(A)`".)  The optimization
    routines now return the last iterates when returning with status
    :const:`'unknown'`, and  provide information about the accuracy of the
    solution they return.  An element-wise max and min of matrices.  Schur
    factorization routines from LAPACK.

**Version 1.0** (April 24, 2008).
    Addition of two-dimensional discrete transforms.  Performance
    improvements in the optimization routines.  Interfaces to the MOSEK and
    GLPK integer LP solvers (these features are documented in the source
    docstrings).

**Version 0.9.3** (February 24, 2008).
    A new solver for quadratic programming with linear cone constraints.
    Minor changes to the other solvers: the option of requesting several
    steps of iterative refinement when solving Newton equations; the
    fields ``W['dl']`` and ``W['dli']`` in the scaling dictionary described
    in section 9.4 were renamed ``W['d']`` and ``W['di']``.

**Version 0.9.2** (December 27, 2007).
    The GNU Scientific Library is no longer required for installation.
    The :mod:`cvxopt.random` module has been deleted, and the functions for
    generating random matrices (:func:`random.uniform`,
    :func:`random.normal`, :func:`random.getseed`, :func:`random.setseed`)
    have been moved to :mod:`cvxopt.base`.  The upgrade also includes an
    improved and more easily customized style of matrix formatting.

**Version 0.9.1** (November 23, 2007).
    A revision of the nonlinear optimization solver, with added support for
    second-order cone and linear matrix inequality constraints.  (A new
    argument was added to the function :func:`solvers.cp()`, but code that
    uses the previous version should still work if the arguments ``A`` and
    ``b`` are specified by keywords.)  The functions in
    :mod:`cvxopt.random` are now based on the random number generators of
    the GNU Scientific Library.  The MOSEK interface was upgraded to
    version 5.  A new function :func:`base.spdiag()` for specifying sparse
    block diagonal matrices.

**Version 0.9** (August 10, 2007).
    A new cone program solver, with support for second-order cone
    constraints.

**Version 0.8.2** (February 6, 2007).
    Performance improvements in the sparse matrix arithmetic. The LAPACK
    solvers for banded and tridiagonal equations. Several bug fixes.

**Version 0.8.1** (October 31, 2006).
    Compatibility with Python 2.5.  An extension of :func:`base.matrix()`
    to construct block matrices.  A new function :func:`sparse()` to create
    sparse block matrices.  The default value of
    :const:`cholmod.options['supernodal']` was changed to 2.

**Version 0.8** (September 20, 2006).
    General sequences are allowed in matrix definitions and assignments.
    The :func:`base.div()`, :func:`base.mul()`, and :func:`base.syrk()`
    functions.  Elementwise exponentiation of dense matrices. The FFTW
    interface.  The optional arguments in BLAS and LAPACK have been
    reordered so that the most important arguments come first. (This
    affects previous code in which optional arguments were passed by
    position instead of by keyword.)  A revised nonlinear convex
    optimization solver with a simpler calling sequence.

**Version 0.7.1** (August 1, 2006).
    Complex sparse matrices.  The sparse BLAS functions :func:`base.symv()`
    and :func:`base.gemm()`.  The DSDP5 interface.
    The :mod:`cvxopt.colamd` and :mod:`cvxopt.ccolamd` interfaces were
    removed.  There are several important backward incompatible changes in
    the definitions of :func:`base.matrix()` and :func:`base.spmatrix()`:

    * The ``x`` argument in :func:`base.matrix()` is now required; it is no
      longer possible to create matrices with uninitialized values.

    * If the ``x`` argument in :func:`base.matrix()` is of integer type,
      an integer matrix is created.  For example, ":samp:`matrix(1)`" now
      creates an :const:`'i'` matrix;  ":samp:`matrix(1.0)`" creates a
      :const:`'d'` matrix.

    * Symmetric sparse matrices are no longer defined. The ``type``
      argument in :func:`base.spmatrix()` has been removed.

    * The ``x``, ``I``, ``J`` arguments in :func:`base.spmatrix()` are all
      required.

**Version 0.7** (April 21, 2006).
    A semidefinite programming solver.  LAPACK routines for QR
    factorization.  The :func:`base.gemv()` function.  The
    :func:`base.smv()` function was removed.

**Version 0.6.1** (February 27, 2006).
    Compatibility with the SciPy array interface.  Portability to 64 bit
    machines.  LAPACK routines for matrix inversion.  Generalized symmetric
    eigenvalue problems and singular value decomposition.  The
    :mod:`cvxopt.ldl` module has been removed.

**Version 0.6** (December 27, 2005).
    Elementwise :func:`exp()`, :func:`sin()`, :func:`cos()`, and
    :func:`log()` of dense matrices.  Indexed assignments of sparse to dense
    matrices.  Pickling of dense and sparse matrices. Interfaces to the
    matrix ordering libraries COLAMD and CCOLAMD.  Several new functions in
    :mod:`cvxopt.cholmod`.  A new LP solver.

**Version 0.5** (October 20, 2005).
    The CHOLMOD interface.  The nonlinear convex optimization solver in the
    solvers module.  Several bug fixes.

**Version 0.4** (May 18, 2005).
    Interfaces to the LP solvers in MOSEK and GLPK.

**Version 0.3** (March 29, 2005).
    Several minor additions and improvements.

**Version 0.2** (January 31, 2005).
    Sparse linear equation solvers from UMFPACK and LDL.  A modeling tool
    for convex piecewise-linear optimization problems.

**Version 0.1** (November 3, 2004).
    Dense and sparse matrix class.  Some BLAS and LAPACK routines.  A linear
    programming solver.
