# -*- coding: utf-8 -*-


"""
Component ArticulatedHierarchyBVHController

.. autofunction:: ArticulatedHierarchyBVHController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ArticulatedHierarchyBVHController(attachedTo , name='ArticulatedHierarchyBVHController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, handleEventTriggersUpdate=0, articulationsIndices=[], bindingKeys=[], angleDelta=0.01, propagateUserInteraction=0, useExternalTime=0, externalTime=0.0, **kwargs):
    """Implements a handler that controls the values of the articulations of an articulated hierarchy container using a .bvh file.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 handleEventTriggersUpdate: Event handling frequency controls the controller update frequency

		 articulationsIndices: Indices of articulations controlled by the keyboard

		 bindingKeys: Keys to press to control the articulations

		 angleDelta: Angle incrementation due to each user interaction

		 propagateUserInteraction: Says wether or not the user interaction is local on the articulations, or must be propagated to children recursively

		 useExternalTime: use the external time line

		 externalTime:  value of the External Time


    """
    return attachedTo.createObject("ArticulatedHierarchyBVHController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, articulationsIndices=articulationsIndices, bindingKeys=bindingKeys, angleDelta=angleDelta, propagateUserInteraction=propagateUserInteraction, useExternalTime=useExternalTime, externalTime=externalTime, **kwargs)
