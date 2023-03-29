# -*- coding: utf-8 -*-


"""
Component AttachBodyButtonSetting

.. autofunction:: AttachBodyButtonSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AttachBodyButtonSetting(attachedTo , name='AttachBodyButtonSetting', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, button='Left', stiffness=1000.0, arrowSize=0.0, showFactorSize=1.0, **kwargs):
    """Attach Body Button configuration


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 button: Mouse button used

		 stiffness: Stiffness of the spring to attach a particule

		 arrowSize: Size of the drawn spring: if >0 an arrow will be drawn

		 showFactorSize: Show factor size of the JointSpringForcefield  when interacting with rigids


    """
    return attachedTo.createObject("AttachBodyButtonSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, button=button, stiffness=stiffness, arrowSize=arrowSize, showFactorSize=showFactorSize, **kwargs)
