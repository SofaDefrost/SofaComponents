# -*- coding: utf-8 -*-


"""
Component SlidingConstraint

.. autofunction:: SlidingConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SlidingConstraint(attachedTo , name='SlidingConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, constraintIndex=0, endTime=-1.0, sliding_point=0, axis_1=0, axis_2=0, force=array([0., 0., 0.]), **kwargs):
    """TODO-SlidingConstraint


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 constraintIndex: Constraint index (first index in the right hand term resolution vector)

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 sliding_point: index of the spliding point on the first model

		 axis_1: index of one end of the sliding axis

		 axis_2: index of the other end of the sliding axis

		 force: force (impulse) used to solve the constraint


    """
    return attachedTo.createObject("SlidingConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, constraintIndex=constraintIndex, endTime=endTime, sliding_point=sliding_point, axis_1=axis_1, axis_2=axis_2, force=force, **kwargs)
