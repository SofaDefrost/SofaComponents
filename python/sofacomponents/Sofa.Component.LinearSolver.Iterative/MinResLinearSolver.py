# -*- coding: utf-8 -*-


"""
Component MinResLinearSolver

.. autofunction:: MinResLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MinResLinearSolver(attachedTo , iterations, tolerance, name='MinResLinearSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, verbose=0, graph='', **kwargs):
    """Linear system solver using the MINRES iterative algorithm


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 iterations: maximum number of iterations of the Conjugate Gradient solution

		 tolerance: desired precision of the Conjugate Gradient Solution (ratio of current residual norm over initial residual norm)

		 verbose: Dump system state at each iteration

		 graph: Graph of residuals at each iteration


    """
    return attachedTo.createObject("MinResLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, iterations=iterations, tolerance=tolerance, verbose=verbose, graph=graph, **kwargs)
