# -*- coding: utf-8 -*-


"""
Component DefaultAnimationLoop

.. autofunction:: DefaultAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DefaultAnimationLoop(attachedTo , name='DefaultAnimationLoop', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, computeBoundingBox=1, **kwargs):
    """Simulation loop to use in scene without constraints nor contact.

This loop do the following steps:
- build and solve all linear systems in the scene : collision and time integration to compute the new values of the dofs
- update the context (dt++)
- update the mappings
- update the bounding box (volume covering all objects of the scene)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 computeBoundingBox: If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.


    """
    return attachedTo.createObject("DefaultAnimationLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, computeBoundingBox=computeBoundingBox, **kwargs)
