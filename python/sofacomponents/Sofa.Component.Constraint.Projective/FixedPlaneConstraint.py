# -*- coding: utf-8 -*-


"""
Component FixedPlaneConstraint

.. autofunction:: FixedPlaneConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FixedPlaneConstraint(attachedTo , name='FixedPlaneConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, direction=array([0., 0., 0.]), dmin=0.0, dmax=0.0, indices=array([], dtype=int32), **kwargs):
    """Project particles on a given plane


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

		 direction: normal direction of the plane

		 dmin: Minimum plane distance from the origin

		 dmax: Maximum plane distance from the origin

		 indices: Indices of the fixed points


    """
    return attachedTo.createObject("FixedPlaneConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, direction=direction, dmin=dmin, dmax=dmax, indices=indices, **kwargs)
