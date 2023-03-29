# -*- coding: utf-8 -*-


"""
Component GenericConstraintSolver

.. autofunction:: GenericConstraintSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GenericConstraintSolver(attachedTo , maxIterations, tolerance, name='GenericConstraintSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, resolutionMethod='ProjectedGaussSeidel', sor=1.0, scaleTolerance=1, allVerified=0, newtonIterations=100, multithreading=0, computeGraphs=0, graphErrors='', graphConstraints='', graphForces='', graphViolations='', currentNumConstraints=0, currentNumConstraintGroups=0, currentIterations=0, currentError=0.0, reverseAccumulateOrder=0, constraintForces=array([], dtype=float64), computeConstraintForces=0, **kwargs):
    """A Generic Constraint Solver using the Linear Complementarity Problem formulation to solve Constraint based components


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 resolutionMethod: Method used to solve the constraint problem, among: "ProjectedGaussSeidel", "UnbuiltGaussSeidel" or "for NonsmoothNonlinearConjugateGradient"

		 maxIterations: maximal number of iterations of the Gauss-Seidel algorithm

		 tolerance: residual error threshold for termination of the Gauss-Seidel algorithm

		 sor: Successive Over Relaxation parameter (0-2)

		 scaleTolerance: Scale the error tolerance with the number of constraints

		 allVerified: All contraints must be verified (each constraint's error < tolerance)

		 newtonIterations: Maximum iteration number of Newton (for the NonsmoothNonlinearConjugateGradient solver only)

		 multithreading: Build compliances concurrently

		 computeGraphs: Compute graphs of errors and forces during resolution

		 graphErrors: Sum of the constraints' errors at each iteration

		 graphConstraints: Graph of each constraint's error at the end of the resolution

		 graphForces: Graph of each constraint's force at each step of the resolution

		 graphViolations: Graph of each constraint's violation at each step of the resolution

		 currentNumConstraints: OUTPUT: current number of constraints

		 currentNumConstraintGroups: OUTPUT: current number of constraints

		 currentIterations: OUTPUT: current number of constraint groups

		 currentError: OUTPUT: current error

		 reverseAccumulateOrder: True to accumulate constraints from nodes in reversed order (can be necessary when using multi-mappings or interaction constraints not following the node hierarchy)

		 constraintForces: OUTPUT: constraint forces (stored only if computeConstraintForces=True)

		 computeConstraintForces: enable the storage of the constraintForces (default = False).


    """
    return attachedTo.createObject("GenericConstraintSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, resolutionMethod=resolutionMethod, maxIterations=maxIterations, tolerance=tolerance, sor=sor, scaleTolerance=scaleTolerance, allVerified=allVerified, newtonIterations=newtonIterations, multithreading=multithreading, computeGraphs=computeGraphs, graphErrors=graphErrors, graphConstraints=graphConstraints, graphForces=graphForces, graphViolations=graphViolations, currentNumConstraints=currentNumConstraints, currentNumConstraintGroups=currentNumConstraintGroups, currentIterations=currentIterations, currentError=currentError, reverseAccumulateOrder=reverseAccumulateOrder, constraintForces=constraintForces, computeConstraintForces=computeConstraintForces, **kwargs)
