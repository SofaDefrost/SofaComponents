# -*- coding: utf-8 -*-


"""
Component SparseLUSolver

.. autofunction:: SparseLUSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SparseLUSolver(attachedTo , name='SparseLUSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, verbose=0, tolerance=0.001, permutation='None', L_nnz=0, **kwargs):
    """Direct linear solver based on Sparse LU factorization, implemented with the CSPARSE library


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 verbose: Dump system state at each iteration

		 tolerance: tolerance of factorization

		 permutation: Type of fill reducing permutation

		 L_nnz: Number of non-zero values in the lower triangular matrix of the factorization. The lower, the faster the system is solved.


    """
    return attachedTo.createObject("SparseLUSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, verbose=verbose, tolerance=tolerance, permutation=permutation, L_nnz=L_nnz, **kwargs)
