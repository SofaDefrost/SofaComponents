# -*- coding: utf-8 -*-


"""
Component PatchTestMovementConstraint

.. autofunction:: PatchTestMovementConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PatchTestMovementConstraint(attachedTo , name='PatchTestMovementConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, meshIndices=array([], dtype=int32), indices=array([], dtype=int32), beginConstraintTime=0.0, endConstraintTime=20.0, constrainedPoints=array([], shape=(0, 3), dtype=float64), cornerMovements=array([], shape=(0, 3), dtype=float64), cornerPoints=array([], shape=(0, 3), dtype=float64), drawConstrainedPoints=0, **kwargs):
    """bilinear constraint


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

		 meshIndices: Indices of the mesh

		 indices: Indices of the constrained points

		 beginConstraintTime: Begin time of the bilinear constraint

		 endConstraintTime: End time of the bilinear constraint

		 constrainedPoints: Coordinates of the constrained points

		 cornerMovements: movements of the corners of the grid

		 cornerPoints: corner points for computing constraint

		 drawConstrainedPoints: draw constrained points


    """
    return attachedTo.createObject("PatchTestMovementConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, meshIndices=meshIndices, indices=indices, beginConstraintTime=beginConstraintTime, endConstraintTime=endConstraintTime, constrainedPoints=constrainedPoints, cornerMovements=cornerMovements, cornerPoints=cornerPoints, drawConstrainedPoints=drawConstrainedPoints, **kwargs)
