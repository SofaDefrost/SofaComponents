# -*- coding: utf-8 -*-


"""
Component EdgeSetController

.. autofunction:: EdgeSetController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EdgeSetController(attachedTo , name='EdgeSetController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, handleEventTriggersUpdate=0, index=0, onlyTranslation=0, buttonDeviceState=0, mainDirection=[[0.0, 0.0, -1.0]], step=0.1, minLength=1.0, maxLength=200.0, maxDepl=0.5, speed=0.0, reversed=0, startingIndex=0, **kwargs):
    """

    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 handleEventTriggersUpdate: Event handling frequency controls the controller update frequency

		 index: Index of the controlled DOF

		 onlyTranslation: Controlling the DOF only in translation

		 buttonDeviceState: state of ths device button

		 mainDirection: Main direction and orientation of the controlled DOF

		 step: base step when changing beam length

		 minLength: min beam length

		 maxLength: max beam length

		 maxDepl: max depl when changing beam length

		 speed: continuous beam length increase/decrease

		 reversed: Extend or retract edgeSet from end

		 startingIndex: index of the edge where a topological change occurs (negative for index relative to last point)


    """
    return attachedTo.createObject("EdgeSetController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, index=index, onlyTranslation=onlyTranslation, buttonDeviceState=buttonDeviceState, mainDirection=mainDirection, step=step, minLength=minLength, maxLength=maxLength, maxDepl=maxDepl, speed=speed, reversed=reversed, startingIndex=startingIndex, **kwargs)
