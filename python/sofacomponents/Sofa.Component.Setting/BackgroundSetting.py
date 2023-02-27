# -*- coding: utf-8 -*-


"""
Component BackgroundSetting

.. autofunction:: BackgroundSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BackgroundSetting(attachedTo , name='BackgroundSetting', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, color=array([1., 1., 1., 1.], dtype=float32), image='', **kwargs):
    """Background setting


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 color: Color of the background

		 image: Image to be used as background


    """
    return attachedTo.createObject("BackgroundSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, color=color, image=image, **kwargs)
