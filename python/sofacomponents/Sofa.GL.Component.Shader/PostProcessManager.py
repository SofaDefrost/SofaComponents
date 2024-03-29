# -*- coding: utf-8 -*-


"""
Component PostProcessManager

.. autofunction:: PostProcessManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PostProcessManager(attachedTo , name='PostProcessManager', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, zNear=1.0, zFar=100.0, **kwargs):
    """PostProcessManager


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 zNear: Set zNear distance (for Depth Buffer)

		 zFar: Set zFar distance (for Depth Buffer)


    """
    return attachedTo.createObject("PostProcessManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, zNear=zNear, zFar=zFar, **kwargs)
