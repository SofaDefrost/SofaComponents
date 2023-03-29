# -*- coding: utf-8 -*-


"""
Component ConstraintAnimationLoop

.. autofunction:: ConstraintAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ConstraintAnimationLoop(attachedTo , name='ConstraintAnimationLoop', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, computeBoundingBox=1, displayTime=0, tolerance=1e-05, maxIterations=1000, doCollisionsFirst=0, doubleBuffer=0, scaleTolerance=1, allVerified=0, sor=1.0, schemeCorrection=0, realTimeCompensation=0, graphErrors='', graphConstraints='', graphForces='', **kwargs):
    """Constraint animation loop manager


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 computeBoundingBox: If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.

		 displayTime: Display time for each important step of ConstraintAnimationLoop.

		 tolerance: Tolerance of the Gauss-Seidel

		 maxIterations: Maximum number of iterations of the Gauss-Seidel

		 doCollisionsFirst: Compute the collisions first (to support penality-based contacts)

		 doubleBuffer: Buffer the constraint problem in a doublebuffer to be accessible with an other thread

		 scaleTolerance: Scale the error tolerance with the number of constraints

		 allVerified: All contraints must be verified (each constraint's error < tolerance)

		 sor: Successive Over Relaxation parameter (0-2)

		 schemeCorrection: Apply new scheme where compliance is progressively corrected

		 realTimeCompensation: If the total computational time T < dt, sleep(dt-T)

		 graphErrors: Sum of the constraints' errors at each iteration

		 graphConstraints: Graph of each constraint's error at the end of the resolution

		 graphForces: Graph of each constraint's force at each step of the resolution


    """
    return attachedTo.createObject("ConstraintAnimationLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, computeBoundingBox=computeBoundingBox, displayTime=displayTime, tolerance=tolerance, maxIterations=maxIterations, doCollisionsFirst=doCollisionsFirst, doubleBuffer=doubleBuffer, scaleTolerance=scaleTolerance, allVerified=allVerified, sor=sor, schemeCorrection=schemeCorrection, realTimeCompensation=realTimeCompensation, graphErrors=graphErrors, graphConstraints=graphConstraints, graphForces=graphForces, **kwargs)
