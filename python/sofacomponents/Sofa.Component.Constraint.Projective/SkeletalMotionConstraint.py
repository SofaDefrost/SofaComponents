# -*- coding: utf-8 -*-


"""
Component SkeletalMotionConstraint

.. autofunction:: SkeletalMotionConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SkeletalMotionConstraint(attachedTo , name='SkeletalMotionConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, joints='[]', bones='[]', animationSpeed=1.0, active=1, **kwargs):
    """animate a skeleton


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

		 joints: skeleton joints

		 bones: skeleton bones

		 animationSpeed: animation speed

		 active: is the constraint active?


    """
    return attachedTo.createObject("SkeletalMotionConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, joints=joints, bones=bones, animationSpeed=animationSpeed, active=active, **kwargs)
