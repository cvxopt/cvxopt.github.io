.. role: raw-html(raw)
   :format: html

Generating random sparse matrices
"""""""""""""""""""""""""""""""""

.. raw:: html

    <p>
    <a href="src/sprandmtrx.py">source code</a>
    </p>

:: 

    from cvxopt import matrix, spmatrix, normal
    import random 

    def sp_rand(m,n,a):

         ''' 
         Generates an mxn sparse 'd' matrix with round(a*m*n) nonzeros.
         '''
      
         if m == 0 or n == 0: return spmatrix([], [], [], (m,n))
         nnz = min(max(0, int(round(a*m*n))), m*n)
         nz = matrix(random.sample(xrange(m*n), nnz), tc='i')
         return spmatrix(normal(nnz,1), nz%m, nz/m, (m,n))
