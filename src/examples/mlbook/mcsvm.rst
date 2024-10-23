.. role: raw-html(raw)
   :format: html


Multiclass SVM
==============

Crammer and Singer (2001) have extended the binary SVM classifier to
classification problems with more than two classes. The training
problem of the Crammer-Singer multiclass SVM can be expressed as a QP
    
.. math:: :label: multiclass_svm

   \begin{array}{ll}	
   \mbox{maximize}   &  -(1/2)  \mathbf{Tr}(U^TQU)  + \mathbf{Tr}(E^TU) \\
   \mbox{subject to} & U \preceq \gamma E \\
                     & U \mathbf{1}_m = 0
   \end{array}

with variable :math:`U \in \mathbf{R}^{N \times m}` where :math:`N` is
the number of training examples and :math:`m` the number of
classes. The :math:`N \times N` kernel matrix :math:`Q` is given by
:math:`Q_{ij} = K(x_i, x_j)` where :math:`K` is a kernel function and
:math:`x_i^T` is the i'th row of the :math:`N \times n` data matrix
:math:`X`, and :math:`d` is an :math:`N`-vector with labels (*i.e.*
:math:`d_i \in \{ 0,1,\ldots,m-1 \}`).



.. raw:: html

   <h3> Documentation </h3>


A custom solver for the multiclass support vector machine training
problem is available as a Python module :download:`mcsvm <mcsvm.py>`. The module
implements the following function:

   .. function:: mcsvm(X, labels, gamma, kernel = 'linear', sigma = 1.0, degree = 1)

      Solves the problem :eq:`multiclass_svm` using a custom KKT solver.

      The input arguments are the data matrix :math:`X` (with the
      :math:`N` training examples :math:`x_i^T` as rows), the label
      vector :math:`d`, and the positive parameter :math:`\gamma`.

      Valid kernel functions are:

      :const:`'linear'`
         the linear kernel: :math:`K(x_i,x_j) = x_i^Tx_j`

      :const:`'poly'`
      	 the polynomial kernel: :math:`K(x_i,x_j) = (x_i^Tx_j/\sigma)^d` 

      The kernel parameters :math:`\sigma` and :math:`d` are specified
      using the input arguments `sigma` and `degree`, respectively.

      Returns the function :func:`classifier`.  If :math:`Y` is
      :math:`M \times n` then `classifier(Y)` returns a list with as
      its k'th element

      .. math::

         \operatorname*{arg\,max}_{j=0,\ldots,m-1}  \sum_{i=1}^N U_{ij} K(x_i, y_k) 

      where :math:`y_k^T` is row :math:`k` of :math:`Y`, :math:`x_i^T`
      is row :math:`k` of :math:`X`, and :math:`U` is the optimal
      solution of the QP :eq:`multiclass_svm`.


.. _mlbook-robust-svm:
   
