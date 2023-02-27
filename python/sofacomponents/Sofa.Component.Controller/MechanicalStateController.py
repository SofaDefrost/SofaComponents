# -*- coding: utf-8 -*-


"""
Component MechanicalStateController

.. autofunction:: MechanicalStateController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MechanicalStateController(attachedTo , name='MechanicalStateController', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, handleEventTriggersUpdate=0, index=0, onlyTranslation=0, buttonDeviceState=0, mainDirection=array([ 0.,  0., -1.]), **kwargs):
    """Provides a Mouse & Keyboard user control on a Mechanical State.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 handleEventTriggersUpdate: Event handling frequency controls the controller update frequency

		 index: Index of the controlled DOF

		 onlyTranslation: Controlling the DOF only in translation

		 buttonDeviceState: state of ths device button

		 mainDirection: Main direction and orientation of the controlled DOF


    """
    return attachedTo.createObject("MechanicalStateController" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, index=index, onlyTranslation=onlyTranslation, buttonDeviceState=buttonDeviceState, mainDirection=mainDirection, **kwargs)
