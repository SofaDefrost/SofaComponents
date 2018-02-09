# -*- coding: utf-8 -*-


"""
Component ArticulatedHierarchyController

.. autofunction:: ArticulatedHierarchyController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ArticulatedHierarchyController(attachedTo , name='ArticulatedHierarchyController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, handleEventTriggersUpdate=0, articulationsIndices=[], bindingKeys=[], angleDelta=0.01, propagateUserInteraction=0, **kwargs):
    """Implements an user interaction handler that controls the values of the articulations of an articulated hierarchy container.


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


    """
    return attachedTo.createObject("ArticulatedHierarchyController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, articulationsIndices=articulationsIndices, bindingKeys=bindingKeys, angleDelta=angleDelta, propagateUserInteraction=propagateUserInteraction, **kwargs)
