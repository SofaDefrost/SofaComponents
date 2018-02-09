# -*- coding: utf-8 -*-


"""
Component GraspingManager

.. autofunction:: GraspingManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GraspingManager(attachedTo , name='GraspingManager', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, active=0, key=49, keySwitch=52, openAngle=1.0, closedAngle=0.0, **kwargs):
    """Manager handling Grasping operations between a SphereModel and a TriangleSetModel relying on a TetrahedronSetTopology


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 active: Activate this object.
Note that this can be dynamically controlled by using a key

		 key: key to press to activate this object until the key is released

		 keySwitch: key to activate this object until the key is pressed again

		 openAngle: angle values to set when tool is opened

		 closedAngle: angle values to set when tool is closed


    """
    return attachedTo.createObject("GraspingManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, active=active, key=key, keySwitch=keySwitch, openAngle=openAngle, closedAngle=closedAngle, **kwargs)
