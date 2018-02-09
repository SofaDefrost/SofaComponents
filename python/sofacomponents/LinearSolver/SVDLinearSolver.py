# -*- coding: utf-8 -*-


"""
Component SVDLinearSolver

.. autofunction:: SVDLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SVDLinearSolver(attachedTo , name='SVDLinearSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, verbose=0, minSingularValue=1e-06, conditionNumber=0.0, **kwargs):
    """Linear system solver using the conjugate gradient iterative algorithm


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 verbose: Dump system state at each iteration

		 minSingularValue: Thershold under which a singular value is set to 0, for the stabilization of ill-conditioned system.

		 conditionNumber: Condition number of the matrix: ratio between the largest and smallest singular values. Computed in method solve.


    """
    return attachedTo.createObject("SVDLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, verbose=verbose, minSingularValue=minSingularValue, conditionNumber=conditionNumber, **kwargs)
