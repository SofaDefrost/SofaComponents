# -*- coding: utf-8 -*-


"""
Component LocalMinDistance

.. autofunction:: LocalMinDistance

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LocalMinDistance(attachedTo , alarmDistance, contactDistance, name='LocalMinDistance', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, filterIntersection=1, angleCone=0.0, coneFactor=0.5, useLMDFilters=0, **kwargs):
    """A set of methods to compute (for constraint methods) if two primitives are close enough to consider they collide


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 alarmDistance: Proximity detection distance

		 contactDistance: Distance below which a contact is created

		 filterIntersection: Activate LMD filter

		 angleCone: Filtering cone extension angle

		 coneFactor: Factor for filtering cone angle computation

		 useLMDFilters: Use external cone computation (Work in Progress)


    """
    return attachedTo.createObject("LocalMinDistance" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, alarmDistance=alarmDistance, contactDistance=contactDistance, filterIntersection=filterIntersection, angleCone=angleCone, coneFactor=coneFactor, useLMDFilters=useLMDFilters, **kwargs)
