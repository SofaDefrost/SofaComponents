# -*- coding: utf-8 -*-


"""
Component ParabolicConstraint

.. autofunction:: ParabolicConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ParabolicConstraint(attachedTo , name='ParabolicConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, indices=array([], dtype=int32), P1=array([0., 0., 0.]), P2=array([0., 0., 0.]), P3=array([0., 0., 0.]), BeginTime=0.0, EndTime=0.0, **kwargs):
    """Apply a parabolic trajectory to given points


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

		 P1: first point of the parabol

		 P2: second point of the parabol

		 P3: third point of the parabol

		 BeginTime: Begin Time of the motion

		 EndTime: End Time of the motion


    """
    return attachedTo.createObject("ParabolicConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, indices=indices, P1=P1, P2=P2, P3=P3, BeginTime=BeginTime, EndTime=EndTime, **kwargs)
