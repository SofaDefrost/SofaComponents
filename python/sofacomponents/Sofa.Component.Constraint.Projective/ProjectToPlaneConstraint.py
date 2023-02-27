# -*- coding: utf-8 -*-


"""
Component ProjectToPlaneConstraint

.. autofunction:: ProjectToPlaneConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ProjectToPlaneConstraint(attachedTo , name='ProjectToPlaneConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, indices=array([0], dtype=int32), origin=array([0., 0., 0.]), normal=array([0., 0., 0.]), drawSize=0.0, **kwargs):
    """Attach given particles to their initial positions


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 indices: Indices of the fixed points

		 origin: A point in the plane

		 normal: Normal vector to the plane

		 drawSize: 0 -> point based rendering, >0 -> radius of spheres


    """
    return attachedTo.createObject("ProjectToPlaneConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, indices=indices, origin=origin, normal=normal, drawSize=drawSize, **kwargs)
