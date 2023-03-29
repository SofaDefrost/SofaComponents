# -*- coding: utf-8 -*-


"""
Component LinearMovementConstraint

.. autofunction:: LinearMovementConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LinearMovementConstraint(attachedTo , name='LinearMovementConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, indices=array([0], dtype=int32), keyTimes=array([0.]), movements=array([[0., 0., 0.]]), relativeMovements=1, showMovement=0, **kwargs):
    """translate given particles


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

		 indices: Indices of the constrained points

		 keyTimes: key times for the movements

		 movements: movements corresponding to the key times

		 relativeMovements: If true, movements are relative to first position, absolute otherwise

		 showMovement: Visualization of the movement to be applied to constrained dofs.


    """
    return attachedTo.createObject("LinearMovementConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, indices=indices, keyTimes=keyTimes, movements=movements, relativeMovements=relativeMovements, showMovement=showMovement, **kwargs)
