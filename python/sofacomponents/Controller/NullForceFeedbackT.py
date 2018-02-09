# -*- coding: utf-8 -*-


"""
Component NullForceFeedbackT

.. autofunction:: NullForceFeedbackT

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NullForceFeedbackT(attachedTo , name='NullForceFeedbackT', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, activate=0, indice=0, **kwargs):
    """Null force feedback for haptic feedback device


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 activate: boolean to activate or deactivate the forcefeedback

		 indice: Tool indice in the OmniDriver


    """
    return attachedTo.createObject("NullForceFeedbackT" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, activate=activate, indice=indice, **kwargs)
