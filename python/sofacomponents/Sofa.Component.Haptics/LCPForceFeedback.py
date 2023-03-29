# -*- coding: utf-8 -*-


"""
Component LCPForceFeedback

.. autofunction:: LCPForceFeedback

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LCPForceFeedback(attachedTo , name='LCPForceFeedback', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, activate=0, indice=0, forceCoef=0.03, solverTimeout=0.0008, solverMaxIt=100, derivRotations=0, localHapticConstraintAllFrames=0, **kwargs):
    """LCP force feedback for the device


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 activate: boolean to activate or deactivate the forcefeedback

		 indice: Tool indice in the OmniDriver

		 forceCoef: multiply haptic force by this coef.

		 solverTimeout: max time to spend solving constraints.

		 solverMaxIt: max iteration to spend solving constraints

		 derivRotations: if true, deriv the rotations when updating the violations

		 localHapticConstraintAllFrames: Flag to enable/disable constraint haptic influence from all frames


    """
    return attachedTo.createObject("LCPForceFeedback" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, activate=activate, indice=indice, forceCoef=forceCoef, solverTimeout=solverTimeout, solverMaxIt=solverMaxIt, derivRotations=derivRotations, localHapticConstraintAllFrames=localHapticConstraintAllFrames, **kwargs)
