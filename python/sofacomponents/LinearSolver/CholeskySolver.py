# -*- coding: utf-8 -*-


"""
Component CholeskySolver

.. autofunction:: CholeskySolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CholeskySolver(attachedTo , name='CholeskySolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, verbose=0, **kwargs):
    """NewMat direct linear solver based on Cholesky factorization, for dense matrices
Direct linear solver based on Cholesky factorization, for dense matrices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 verbose: Dump system state at each iteration


    """
    return attachedTo.createObject("CholeskySolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, verbose=verbose, **kwargs)
