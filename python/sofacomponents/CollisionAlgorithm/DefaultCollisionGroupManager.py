# -*- coding: utf-8 -*-


"""
Component DefaultCollisionGroupManager

.. autofunction:: DefaultCollisionGroupManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DefaultCollisionGroupManager(attachedTo , name='DefaultCollisionGroupManager', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, **kwargs):
    """Responsible for gathering colliding objects in the same group, for consistent time integration


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("DefaultCollisionGroupManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, **kwargs)
