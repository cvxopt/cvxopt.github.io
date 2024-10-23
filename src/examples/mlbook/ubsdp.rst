.. role: raw-html(raw)
   :format: html

SDPs with upper bounds
======================

Consider a standard form SDP with an added upper bound 

.. math:: :label: ubsdp

   \begin{array}{ll}	
   \mbox{minimize}   & \mathbf{Tr}(BX) \\
   \mbox{subject to} & \mathbf{Tr}(A_iX) + c_i = 0, \quad i =
   		        1,\ldots, n \\
	             & 0 \preceq X \preceq I 
   \end{array}

with variable :math:`X \in \mathbf{S}^m`. The problem :eq:`ubsdp` can be reformulated by introducing a slack variable :math:`S`

.. math:: :label: ubsdp_2

   \begin{array}{ll}	
   \mbox{minimize}   & \mathbf{Tr}(BX) \\
   \mbox{subject to} & \mathbf{Tr}(A_iX) + c_i = 0, \quad i =
   		        1,\ldots, n \\
	 	     & X + S = I \\
	             & X \succeq 0, \ S \succeq 0.
   \end{array}

.. raw:: html

   <h3> Documentation </h3>

A custom solver for SDPs with upper bounds is available as a Python
module :download:`ubsdp.py <ubsdp.py>`. The  module implements the following function:

   .. function:: ubsdp(c, A, B, pstart = None, dstart = None)

      Solves the problem :eq:`ubsdp_2` using a custom KKT solver.

      The input arguments are :math:`c \in \mathbf{R}^n`, a matrix
      :math:`A \in \mathbf{R}^{m^2 \times n}`, and a matrix :math:`B
      \in \mathbf{S}^m`. The columns of :math:`A` are
      :math:`\mathbf{vec}(A_i)` where :math:`A_i \in \mathbf{S}^m` is
      the i'th data matrix.

      Returns the solution :math:`X`.


.. raw:: html

   <h3> Example </h3>

::

   from cvxopt import matrix, normal, spdiag, misc, lapack
   from ubsdp import ubsdp

   m, n = 50, 50
   A = normal(m**2, n)

   # Z0 random positive definite with maximum e.v. less than 1.0.
   Z0 = normal(m,m)
   Z0 = Z0 * Z0.T
   w = matrix(0.0, (m,1))   
   a = +Z0
   lapack.syev(a, w, jobz = 'V')
   wmax = max(w) 
   if wmax > 0.9:  w = (0.9/wmax) * w
   Z0 = a * spdiag(w) * a.T

   # c = -A'(Z0)
   c = matrix(0.0, (n,1))
   misc.sgemv(A, Z0, c, dims = {'l': 0, 'q': [], 's': [m]}, trans = 'T', alpha = -1.0)

   # Z1 = I - Z0
   Z1 = -Z0
   Z1[::m+1] += 1.0

   x0 = normal(n,1)
   X0 = normal(m,m)
   X0 = X0*X0.T
   S0 = normal(m,m)
   S0 = S0*S0.T
   # B = A(x0) - X0 + S0
   B = matrix(A*x0 - X0[:] + S0[:], (m,m))

   X = ubsdp(c, A, B)

