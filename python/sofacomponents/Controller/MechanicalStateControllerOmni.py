# -*- coding: utf-8 -*-


"""
Component MechanicalStateControllerOmni

.. autofunction:: MechanicalStateControllerOmni

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MechanicalStateControllerOmni(attachedTo , name='MechanicalStateControllerOmni', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, handleEventTriggersUpdate=0, buttonDeviceState=0, deviceId=-1, angle=10.0, speed=30.0, **kwargs):
    """Provides an Omni user control on a Mechanical State.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 handleEventTriggersUpdate: Event handling frequency controls the controller update frequency

		 buttonDeviceState: state of ths device button

		 deviceId: id of active device for this controller

		 angle: max angle

		 speed: closing/opening speed


    """
    return attachedTo.createObject("MechanicalStateControllerOmni" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, buttonDeviceState=buttonDeviceState, deviceId=deviceId, angle=angle, speed=speed, **kwargs)
