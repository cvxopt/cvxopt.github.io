.. role: raw-html(raw)
   :format: html

L1-norm regularized least-squares
=============================================

We consider a least-squares problem with :math:`\ell_1`-norm
regularization

.. math:: :label: regls

   \begin{array}{ll}	
   \mbox{minimize}   &  \| Ax - b \|_2^2  + \| x \|_1 
   \end{array}

with variable :math:`x \in \mathbf{R}^n` and problem data :math:`A \in \mathbf{R}^{m \times n}` and :math:`b \in
\mathbf{R}^m`. The problem is equivalent to a QP

.. math:: :label: regls_qp

   \begin{array}{ll}	
   \mbox{minimize}   & \| Ax - b \|_2^2  +  \mathbf{1}^Tv\\
   \mbox{subject to} & -v \preceq x \preceq v 
   \end{array}

with :math:`2n` variables and :math:`2n` constraints. The problem can
also be written as a separable QP

.. math:: :label: regls_qp2

   \begin{array}{ll}	
   \mbox{minimize}   & w^Tw + e^Tu\\
   \mbox{subject to} & -u \preceq x \preceq u \\
   		     & Ax - w = b.
   \end{array}
            

.. raw:: html

   <h3> Documentation </h3>

Solvers for the :math:`\ell_1`-norm regularized least-squares problem are
available as a Python module :download:`l1regls.py <l1regls.py>`
(or :download:`l1regls_mosek6.py <l1regls_mosek6.py>` or :download:`l1regls_mosek7.py` for earlier versions of CVXOPT that use MOSEK 6 or 7). The module implements the following three functions:

   .. function:: l1regls(A,b)

      Solves the problem :eq:`regls_qp` using a custom KKT solver.

      Returns the solution :math:`x`. 

   .. function:: l1regls_mosek(A, b)

      Solves the problem :eq:`regls_qp` using MOSEK. This function is
      only available if MOSEK is installed.

      Returns the solution :math:`x`. 

   .. function:: l1regls_mosek2(A, b)

      Solves the problem :eq:`regls_qp2` using MOSEK. This function is
      only available if MOSEK is installed.

      Returns the solution :math:`x`. 

.. raw:: html

   <h3> Example </h3>

::

  from l1regls import l1regls
  from cvxopt import normal

  m, n = 50, 200 
  A, b = normal(m,n), normal(m,1)
  x = l1regls(A,b)
