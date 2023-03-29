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

        
def CGLinearSolver(attachedTo , iterations, tolerance, threshold, name='CGLinearSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, warmStart=0, graph='', **kwargs):
    """Linear system solver using the conjugate gradient iterative algorithm


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 iterations: Maximum number of iterations of the Conjugate Gradient solution

		 tolerance: Desired accuracy of the Conjugate Gradient solution evaluating: |r|²/|b|² (ratio of current residual norm over initial residual norm)

		 threshold: Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution

		 warmStart: Use previous solution as initial solution

		 graph: Graph of residuals at each iteration


    """
    return attachedTo.createObject("CGLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, iterations=iterations, tolerance=tolerance, threshold=threshold, warmStart=warmStart, graph=graph, **kwargs)
