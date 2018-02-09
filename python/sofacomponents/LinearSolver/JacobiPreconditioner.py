# -*- coding: utf-8 -*-


"""
Component JacobiPreconditioner

.. autofunction:: JacobiPreconditioner

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def JacobiPreconditioner(attachedTo , name='JacobiPreconditioner', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, verbose=0, **kwargs):
    """Linear solver based on a diagonal matrix (i.e. Jacobi preconditioner)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 verbose: Dump system state at each iteration


    """
    return attachedTo.createObject("JacobiPreconditioner" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, verbose=verbose, **kwargs)
