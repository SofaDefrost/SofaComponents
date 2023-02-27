# -*- coding: utf-8 -*-


"""
Component NullForceFeedback

.. autofunction:: NullForceFeedback

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NullForceFeedback(attachedTo , name='NullForceFeedback', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, activate=0, indice=0, **kwargs):
    """Null force feedback for haptic feedback device


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 activate: boolean to activate or deactivate the forcefeedback

		 indice: Tool indice in the OmniDriver


    """
    return attachedTo.createObject("NullForceFeedback" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, activate=activate, indice=indice, **kwargs)
