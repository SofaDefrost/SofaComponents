# -*- coding: utf-8 -*-


"""
Component VisualStyle

.. autofunction:: VisualStyle

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VisualStyle(attachedTo , name='VisualStyle', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, displayFlags='', **kwargs):
    """Edit the visual style.
 Allowed values for displayFlags data are a combination of the following:
showAll, hideAll,
    showVisual, hideVisual,
        showVisualModels, hideVisualModels,
    showBehavior, hideBehavior,
        showBehaviorModels, hideBehaviorModels,
        showForceFields, hideForceFields,
        showInteractionForceFields, hideInteractionForceFields
    showMapping, hideMapping
        showMappings, hideMappings
        showMechanicalMappings, hideMechanicalMappings
    showCollision, hideCollision
        showCollisionModels, hideCollisionModels
        showBoundingCollisionModels, hideBoundingCollisionModels
    showOptions hideOptions
        showRendering hideRendering
        showNormals hideNormals
        showWireframe hideWireframe


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 displayFlags: Display Flags


    """
    return attachedTo.createObject("VisualStyle" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, displayFlags=displayFlags, **kwargs)
