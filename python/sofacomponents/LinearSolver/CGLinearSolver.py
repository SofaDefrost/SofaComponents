# -*- coding: utf-8 -*-


"""
Component CGLinearSolver

.. autofunction:: CGLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CGLinearSolver(attachedTo , iterations, tolerance, threshold, name='CGLinearSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, warmStart=0, verbose=0, graph='', **kwargs):
    """Linear system solver using the conjugate gradient iterative algorithm
NewMat linear system solver using the conjugate gradient iterative algorithm


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 iterations: Maximum number of iterations of the Conjugate Gradient solution

		 tolerance: Desired accuracy of the Conjugate Gradient solution (ratio of current residual norm over initial residual norm)

		 threshold: Minimum value of the denominator in the conjugate Gradient solution

		 warmStart: Use previous solution as initial solution

		 verbose: Dump system state at each iteration

		 graph: Graph of residuals at each iteration


    """
    return attachedTo.createObject("CGLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, iterations=iterations, tolerance=tolerance, threshold=threshold, warmStart=warmStart, verbose=verbose, graph=graph, **kwargs)
