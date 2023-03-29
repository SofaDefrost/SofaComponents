# -*- coding: utf-8 -*-


"""
Component MultiStepAnimationLoop

.. autofunction:: MultiStepAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MultiStepAnimationLoop(attachedTo , name='MultiStepAnimationLoop', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, computeBoundingBox=1, collisionSteps=1, integrationSteps=1, **kwargs):
    """Multi steps animation loop, multi integration steps in a single animation step are managed.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 computeBoundingBox: If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.

		 collisionSteps: number of collision steps between each frame rendering

		 integrationSteps: number of integration steps between each collision detection


    """
    return attachedTo.createObject("MultiStepAnimationLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, computeBoundingBox=computeBoundingBox, collisionSteps=collisionSteps, integrationSteps=integrationSteps, **kwargs)
