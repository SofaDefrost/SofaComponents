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

        
def ShewchukPCGLinearSolver(attachedTo , name='ShewchukPCGLinearSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, multiGroup=0, iterations=25, tolerance=1e-05, use_precond=1, update_step=1, build_precond=1, preconditioners='', graph='', **kwargs):
    """Linear system solver using the conjugate gradient iterative algorithm


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 iterations: maximum number of iterations of the Conjugate Gradient solution

		 tolerance: desired precision of the Conjugate Gradient Solution (ratio of current residual norm over initial residual norm)

		 use_precond: Use preconditioner

		 update_step: Number of steps before the next refresh of precondtioners

		 build_precond: Build the preconditioners, if false build the preconditioner only at the initial step

		 preconditioners: If not empty: path to the solvers to use as preconditioners

		 graph: Graph of residuals at each iteration


    """
    return attachedTo.createObject("ShewchukPCGLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, iterations=iterations, tolerance=tolerance, use_precond=use_precond, update_step=update_step, build_precond=build_precond, preconditioners=preconditioners, graph=graph, **kwargs)
