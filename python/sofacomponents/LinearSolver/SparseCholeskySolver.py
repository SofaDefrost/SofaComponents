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

        
def SparseCholeskySolver(attachedTo , name='SparseCholeskySolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, verbose=0, **kwargs):
    """Direct linear solver based on Sparse Cholesky factorization, implemented with the CSPARSE library


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 verbose: Dump system state at each iteration


    """
    return attachedTo.createObject("SparseCholeskySolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, verbose=verbose, **kwargs)
