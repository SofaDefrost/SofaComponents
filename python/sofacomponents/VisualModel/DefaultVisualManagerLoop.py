# -*- coding: utf-8 -*-


"""
Component DefaultVisualManagerLoop

.. autofunction:: DefaultVisualManagerLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DefaultVisualManagerLoop(attachedTo , name='DefaultVisualManagerLoop', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, **kwargs):
    """The simplest Visual Loop Manager, created by default when user do not put on scene


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("DefaultVisualManagerLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, **kwargs)
