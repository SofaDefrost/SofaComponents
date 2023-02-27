# -*- coding: utf-8 -*-


"""
Component FixedRotationConstraint

.. autofunction:: FixedRotationConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FixedRotationConstraint(attachedTo , name='FixedRotationConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, FixedXRotation=0, FixedYRotation=0, FixedZRotation=0, **kwargs):
    """Prevents rotation around x or/and y or/and z axis


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

		 FixedXRotation: Prevent Rotation around X axis

		 FixedYRotation: Prevent Rotation around Y axis

		 FixedZRotation: Prevent Rotation around Z axis


    """
    return attachedTo.createObject("FixedRotationConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, FixedXRotation=FixedXRotation, FixedYRotation=FixedYRotation, FixedZRotation=FixedZRotation, **kwargs)
