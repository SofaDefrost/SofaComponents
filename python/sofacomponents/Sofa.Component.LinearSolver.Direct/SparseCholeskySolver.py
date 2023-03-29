# -*- coding: utf-8 -*-


"""
Component SparseCholeskySolver

.. autofunction:: SparseCholeskySolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SparseCholeskySolver(attachedTo , name='SparseCholeskySolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, verbose=0, permutation='None', **kwargs):
    """Direct linear solver based on Sparse Cholesky factorization, implemented with the CSPARSE library


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 verbose: Dump system state at each iteration

		 permutation: Type of fill reducing permutation


    """
    return attachedTo.createObject("SparseCholeskySolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, verbose=verbose, permutation=permutation, **kwargs)
