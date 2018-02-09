# -*- coding: utf-8 -*-


"""
Component LMDNewProximityIntersection

.. autofunction:: LMDNewProximityIntersection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LMDNewProximityIntersection(attachedTo , alarmDistance, contactDistance, name='LMDNewProximityIntersection', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, useLineLine=1, **kwargs):
    """Filtered optimized proximity intersection.


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
    return attachedTo.createObject("LMDNewProximityIntersection" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, alarmDistance=alarmDistance, contactDistance=contactDistance, useLineLine=useLineLine, **kwargs)
