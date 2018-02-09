# -*- coding: utf-8 -*-


"""
Component LinearVelocityConstraint

.. autofunction:: LinearVelocityConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LinearVelocityConstraint(attachedTo , name='LinearVelocityConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, group=0, endTime=-1.0, indices=[[0]], keyTimes=[[0.0]], velocities=[[0.0, 0.0, 0.0]], coordinates=[], **kwargs):
    """apply velocity to given particles


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 indices: Indices of the constrained points

		 keyTimes: key times for the movements

		 velocities: velocities corresponding to the key times

		 coordinates: coordinates on which to apply velocities


    """
    return attachedTo.createObject("LinearVelocityConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, endTime=endTime, indices=indices, keyTimes=keyTimes, velocities=velocities, coordinates=coordinates, **kwargs)
