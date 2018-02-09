# -*- coding: utf-8 -*-


"""
Component LCPConstraintSolver

.. autofunction:: LCPConstraintSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LCPConstraintSolver(attachedTo , tolerance, maxIt, name='LCPConstraintSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, displayDebug=0, displayTime=0, initial_guess=1, build_lcp=1, mu=0.6, minW=0.0, maxF=0.0, multi_grid=0, multi_grid_levels=2, merge_method=0, merge_spatial_step=2, merge_local_levels=2, group=[[0]], graph='', showLevels=0, showCellWidth=0.0, showTranslation=[[0.0, 0.0, 0.0]], showLevelTranslation=[[0.0, 0.0, 0.0]], **kwargs):
    """A Constraint Solver using the Linear Complementarity Problem formulation to solve BaseConstraint based components


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 displayDebug: Display debug information.

		 displayTime: Display time for each important step of LCPConstraintSolver.

		 initial_guess: activate LCP results history to improve its resolution performances.

		 build_lcp: LCP is not fully built to increase performance in some case.

		 tolerance: residual error threshold for termination of the Gauss-Seidel algorithm

		 maxIt: maximal number of iterations of the Gauss-Seidel algorithm

		 mu: Friction coefficient

		 minW: If not zero, constraints whose self-compliance (i.e. the corresponding value on the diagonal of W) is smaller than this threshold will be ignored

		 maxF: If not zero, constraints whose response force becomes larger than this threshold will be ignored

		 multi_grid: activate multi_grid resolution (NOT STABLE YET)

		 multi_grid_levels: if multi_grid is active: how many levels to create (>=2)

		 merge_method: if multi_grid is active: which method to use to merge constraints (0 = compliance-based, 1 = spatial coordinates)

		 merge_spatial_step: if merge_method is 1: grid size reduction between multigrid levels

		 merge_local_levels: if merge_method is 1: up to the specified level of the multigrid, constraints are grouped locally, i.e. separately within each contact pairs, while on upper levels they are grouped globally independently of contact pairs.

		 group: list of ID of groups of constraints to be handled by this solver.

		 graph: Graph of residuals at each iteration

		 showLevels: Number of constraint levels to display

		 showCellWidth: Distance between each constraint cells

		 showTranslation: Position of the first cell

		 showLevelTranslation: Translation between levels


    """
    return attachedTo.createObject("LCPConstraintSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, displayDebug=displayDebug, displayTime=displayTime, initial_guess=initial_guess, build_lcp=build_lcp, tolerance=tolerance, maxIt=maxIt, mu=mu, minW=minW, maxF=maxF, multi_grid=multi_grid, multi_grid_levels=multi_grid_levels, merge_method=merge_method, merge_spatial_step=merge_spatial_step, merge_local_levels=merge_local_levels, group=group, graph=graph, showLevels=showLevels, showCellWidth=showCellWidth, showTranslation=showTranslation, showLevelTranslation=showLevelTranslation, **kwargs)
