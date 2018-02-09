# -*- coding: utf-8 -*-


"""
Component NewProximityIntersection

.. autofunction:: NewProximityIntersection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NewProximityIntersection(attachedTo , alarmDistance, contactDistance, name='NewProximityIntersection', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, useLineLine=0, **kwargs):
    """Optimized Proximity Intersection based on Triangle-Triangle tests, ignoring Edge-Edge cases


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 alarmDistance: Proximity detection distance

		 contactDistance: Distance below which a contact is created

		 useLineLine: Line-line collision detection enabled


    """
    return attachedTo.createObject("NewProximityIntersection" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, alarmDistance=alarmDistance, contactDistance=contactDistance, useLineLine=useLineLine, **kwargs)
