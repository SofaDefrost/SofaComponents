# -*- coding: utf-8 -*-


"""
Component HermiteSplineConstraint

.. autofunction:: HermiteSplineConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HermiteSplineConstraint(attachedTo , name='HermiteSplineConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, indices=array([], dtype=int32), BeginTime=0.0, EndTime=0.0, X0=array([0., 0., 0.]), dX0=array([0., 0., 0.]), X1=array([0., 0., 0.]), dX1=array([0., 0., 0.]), SX0=array([0., 0.]), SX1=array([0., 0.]), **kwargs):
    """Apply a hermite cubic spline trajectory to given points


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

		 BeginTime: Begin Time of the motion

		 EndTime: End Time of the motion

		 X0: first control point

		 dX0: first control tangente

		 X1: second control point

		 dX1: sceond control tangente

		 SX0: first interpolation vector

		 SX1: second interpolation vector


    """
    return attachedTo.createObject("HermiteSplineConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, indices=indices, BeginTime=BeginTime, EndTime=EndTime, X0=X0, dX0=dX0, X1=X1, dX1=dX1, SX0=SX0, SX1=SX1, **kwargs)
