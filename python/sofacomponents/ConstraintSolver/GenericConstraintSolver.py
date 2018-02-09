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

        
def GenericConstraintSolver(attachedTo , maxIterations, tolerance, name='GenericConstraintSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, displayTime=0, sor=1.0, scaleTolerance=1, allVerified=0, schemeCorrection=0, unbuilt=0, computeGraphs=0, graphErrors='', graphConstraints='', graphForces='', graphViolations='', currentNumConstraints=0, currentNumConstraintGroups=0, currentIterations=0, currentError=0.0, reverseAccumulateOrder=0, **kwargs):
    """A Generic Constraint Solver using the Linear Complementarity Problem formulation to solve Constraint based components


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 displayTime: Display time for each important step of GenericConstraintSolver.

		 maxIterations: maximal number of iterations of the Gauss-Seidel algorithm

		 tolerance: residual error threshold for termination of the Gauss-Seidel algorithm

		 sor: Successive Over Relaxation parameter (0-2)

		 scaleTolerance: Scale the error tolerance with the number of constraints

		 allVerified: All contraints must be verified (each constraint's error < tolerance)

		 schemeCorrection: Apply new scheme where compliance is progressively corrected

		 unbuilt: Compliance is not fully built

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


    """
    return attachedTo.createObject("GenericConstraintSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, displayTime=displayTime, maxIterations=maxIterations, tolerance=tolerance, sor=sor, scaleTolerance=scaleTolerance, allVerified=allVerified, schemeCorrection=schemeCorrection, unbuilt=unbuilt, computeGraphs=computeGraphs, graphErrors=graphErrors, graphConstraints=graphConstraints, graphForces=graphForces, graphViolations=graphViolations, currentNumConstraints=currentNumConstraints, currentNumConstraintGroups=currentNumConstraintGroups, currentIterations=currentIterations, currentError=currentError, reverseAccumulateOrder=reverseAccumulateOrder, **kwargs)
