# -*- coding: utf-8 -*-


"""
Component SparseLDLSolver

.. autofunction:: SparseLDLSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SparseLDLSolver(attachedTo , name='SparseLDLSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, precomputeSymbolicDecomposition=1, applyPermutation=1, L_nnz=0, **kwargs):
    """Direct Linear Solver using a Sparse LDL^T factorization.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 precomputeSymbolicDecomposition: If true the solver will reuse the precomputed symbolic decomposition. Otherwise it will recompute it at each step.

		 applyPermutation: If true the solver will apply a fill-reducing permutation to the matrix of the system.

		 L_nnz: Number of non-zero values in the lower triangular matrix of the factorization. The lower, the faster the system is solved.


    """
    return attachedTo.createObject("SparseLDLSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, precomputeSymbolicDecomposition=precomputeSymbolicDecomposition, applyPermutation=applyPermutation, L_nnz=L_nnz, **kwargs)
