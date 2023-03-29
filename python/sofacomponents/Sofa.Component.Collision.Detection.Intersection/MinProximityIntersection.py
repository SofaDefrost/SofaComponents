# -*- coding: utf-8 -*-


"""
Component MinProximityIntersection

.. autofunction:: MinProximityIntersection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MinProximityIntersection(attachedTo , alarmDistance, contactDistance, name='MinProximityIntersection', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, useSphereTriangle=1, usePointPoint=1, useSurfaceNormals=0, useLinePoint=1, useLineLine=1, **kwargs):
    """A set of methods to compute if two primitives are close enough to consider they collide


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 alarmDistance: Proximity detection distance

		 contactDistance: Distance below which a contact is created

		 useSphereTriangle: activate Sphere-Triangle intersection tests

		 usePointPoint: activate Point-Point intersection tests

		 useSurfaceNormals: Compute the norms of the Detection Outputs by considering the normals of the surfaces involved.

		 useLinePoint: activate Line-Point intersection tests

		 useLineLine: activate Line-Line  intersection tests


    """
    return attachedTo.createObject("MinProximityIntersection" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, alarmDistance=alarmDistance, contactDistance=contactDistance, useSphereTriangle=useSphereTriangle, usePointPoint=usePointPoint, useSurfaceNormals=useSurfaceNormals, useLinePoint=useLinePoint, useLineLine=useLineLine, **kwargs)
