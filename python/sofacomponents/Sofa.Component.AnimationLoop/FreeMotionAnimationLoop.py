# -*- coding: utf-8 -*-


"""
Component FreeMotionAnimationLoop

.. autofunction:: FreeMotionAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FreeMotionAnimationLoop(attachedTo , name='FreeMotionAnimationLoop', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, computeBoundingBox=1, solveVelocityConstraintFirst=0, threadSafeVisitor=0, parallelCollisionDetectionAndFreeMotion=0, parallelODESolving=0, **kwargs):
    """
The animation loop to use with constraints.
You must add this loop at the beginning of the scene if you are using constraints."


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 computeBoundingBox: If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.

		 solveVelocityConstraintFirst: solve separately velocity constraint violations before position constraint violations

		 threadSafeVisitor: If true, do not use realloc and free visitors in fwdInteractionForceField.

		 parallelCollisionDetectionAndFreeMotion: If true, executes free motion step and collision detection step in parallel.

		 parallelODESolving: If true, solves all the ODEs in parallel during the free motion step.


    """
    return attachedTo.createObject("FreeMotionAnimationLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, computeBoundingBox=computeBoundingBox, solveVelocityConstraintFirst=solveVelocityConstraintFirst, threadSafeVisitor=threadSafeVisitor, parallelCollisionDetectionAndFreeMotion=parallelCollisionDetectionAndFreeMotion, parallelODESolving=parallelODESolving, **kwargs)
