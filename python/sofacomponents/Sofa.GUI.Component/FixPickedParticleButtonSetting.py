# -*- coding: utf-8 -*-


"""
Component FixPickedParticleButtonSetting

.. autofunction:: FixPickedParticleButtonSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FixPickedParticleButtonSetting(attachedTo , name='FixPickedParticleButtonSetting', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, button='Left', stiffness=10000.0, **kwargs):
    """Fix a picked particle in space


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 button: Mouse button used

		 stiffness: Stiffness of the spring to fix a particule


    """
    return attachedTo.createObject("FixPickedParticleButtonSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, button=button, stiffness=stiffness, **kwargs)
