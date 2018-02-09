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

        
def SparseLUSolver(attachedTo , name='SparseLUSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, verbose=0, tolerance=0.001, **kwargs):
    """Direct linear solver based on Sparse LU factorization, implemented with the CSPARSE library


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 verbose: Dump system state at each iteration

		 tolerance: tolerance of factorization


    """
    return attachedTo.createObject("SparseLUSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, verbose=verbose, tolerance=tolerance, **kwargs)
