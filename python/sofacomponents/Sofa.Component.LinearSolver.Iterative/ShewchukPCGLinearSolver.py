# -*- coding: utf-8 -*-


"""
Component ShewchukPCGLinearSolver

.. autofunction:: ShewchukPCGLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ShewchukPCGLinearSolver(attachedTo , name='ShewchukPCGLinearSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, iterations=25, tolerance=1e-05, use_precond=1, update_step=1, build_precond=1, graph='', **kwargs):
    """Linear system solver using the conjugate gradient iterative algorithm


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 iterations: maximum number of iterations of the Conjugate Gradient solution

		 tolerance: desired precision of the Conjugate Gradient Solution (ratio of current residual norm over initial residual norm)

		 use_precond: Use preconditioner

		 update_step: Number of steps before the next refresh of precondtioners

		 build_precond: Build the preconditioners, if false build the preconditioner only at the initial step

		 graph: Graph of residuals at each iteration


    """
    return attachedTo.createObject("ShewchukPCGLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, iterations=iterations, tolerance=tolerance, use_precond=use_precond, update_step=update_step, build_precond=build_precond, graph=graph, **kwargs)
