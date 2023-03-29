# -*- coding: utf-8 -*-


"""
Component StaticSolver

.. autofunction:: StaticSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def StaticSolver(attachedTo , name='StaticSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, newton_iterations=1, absolute_correction_tolerance_threshold=1e-05, relative_correction_tolerance_threshold=1e-05, absolute_residual_tolerance_threshold=1e-05, relative_residual_tolerance_threshold=1e-05, should_diverge_when_residual_is_growing=0, **kwargs):
    """Static ODE Solver


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 newton_iterations: Number of newton iterations between each load increments (normally, one load increment per simulation time-step.

		 absolute_correction_tolerance_threshold: Convergence criterion: The newton iterations will stop when the norm |du| is smaller than this threshold.

		 relative_correction_tolerance_threshold: Convergence criterion: The newton iterations will stop when the ratio |du| / |U| is smaller than this threshold.

		 absolute_residual_tolerance_threshold: Convergence criterion: The newton iterations will stop when the norm |R| is smaller than this threshold. Use a negative value to disable this criterion.

		 relative_residual_tolerance_threshold: Convergence criterion: The newton iterations will stop when the ratio |R|/|R0| is smaller than this threshold. Use a negative value to disable this criterion.

		 should_diverge_when_residual_is_growing: Divergence criterion: The newton iterations will stop when the residual is greater than the one from the previous iteration.


    """
    return attachedTo.createObject("StaticSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, newton_iterations=newton_iterations, absolute_correction_tolerance_threshold=absolute_correction_tolerance_threshold, relative_correction_tolerance_threshold=relative_correction_tolerance_threshold, absolute_residual_tolerance_threshold=absolute_residual_tolerance_threshold, relative_residual_tolerance_threshold=relative_residual_tolerance_threshold, should_diverge_when_residual_is_growing=should_diverge_when_residual_is_growing, **kwargs)
