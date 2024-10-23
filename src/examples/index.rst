.. role:: raw-html(raw)
   :format: html

########
Examples 
########

Tutorial examples
=================

Short examples that illustrate basic features of CVXOPT.

.. toctree::

    tutorial/creating-matrices.rst
    tutorial/indexing.rst
    tutorial/numpy.rst
    tutorial/lp.rst
    tutorial/qp.rst


Book examples
=============

Examples from the book 
`Convex Optimization <http://www.stanford.edu/~boyd/cvxbook>`_ by Boyd 
and Vandenberghe.  

.. toctree::

    book/rls.rst
    book/portfolio.rst
    book/penalties.rst
    book/huber.rst
    book/inputdesign.rst
    book/regsel.rst
    book/smoothrec.rst
    book/tv.rst
    book/robls.rst
    book/polapprox.rst
    book/basispursuit.rst
    book/cvxfit.rst
    book/consumerpref.rst
    book/logreg.rst
    book/maxent.rst
    book/probbounds.rst
    book/chernoff.rst
    book/expdesign.rst
    book/ellipsoids.rst
    book/centers.rst
    book/linsep.rst
    book/placement.rst
    book/floorplan.rst


Custom interior-point solvers
=============================

Examples from the book chapter
`Interior-point methods for large-scale cone programming <http://www.ee.ucla.edu/~vandenbe/publications/mlbook.pdf>`_ (pdf) by M. S. Andersen, J. Dahl, Z. Liu, L. Vandenberghe; in: S. Sra, S. Nowozin, S. J. Wright (Editors) Optimization for Machine Learning, MIT Press, 2011.

.. toctree::
   :maxdepth: 2

   mlbook/l1.rst
   mlbook/l1regls.rst
   mlbook/mcsvm.rst
   mlbook/robsvm.rst
   mlbook/ubsdp.rst

The code for nuclear norm approximation can be found :doc:`here </applications/nucnrm/index>`.



Utility functions
=================

Useful Python scripts that are not included in the distribution.

- Generating random sparse matrices (:download:`sprandmtrx.py <sprandmtrx.py>`) 
- Reading and writing Matlab mat-files (:download:`matfile.py <matfile.py>`; Python 2.7 only)


Other examples
==============

.. toctree::

    other/embed_cvxopt.rst
