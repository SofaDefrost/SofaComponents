# -*- coding: utf-8 -*-


"""
Component BilateralInteractionConstraint

.. autofunction:: BilateralInteractionConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BilateralInteractionConstraint(attachedTo , name='BilateralInteractionConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, group=0, constraintIndex=0, endTime=-1.0, first_point=array([], dtype=int32), second_point=array([], dtype=int32), rest_vector=array([], shape=(0, 3), dtype=float64), numericalTolerance=0.0001, activate=1, keepOrientationDifference=0, **kwargs):
    """BilateralInteractionConstraint defining an holonomic equality constraint (attachment)


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

		 first_point: index of the constraint on the first model

		 second_point: index of the constraint on the second model

		 rest_vector: Relative position to maintain between attached points (optional)

		 numericalTolerance: a real value specifying the tolerance during the constraint solving. (optional, default=0.0001)

		 activate: control constraint activation (true by default)

		 keepOrientationDifference: keep the initial difference in orientation (only for rigids)


    """
    return attachedTo.createObject("BilateralInteractionConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, constraintIndex=constraintIndex, endTime=endTime, first_point=first_point, second_point=second_point, rest_vector=rest_vector, numericalTolerance=numericalTolerance, activate=activate, keepOrientationDifference=keepOrientationDifference, **kwargs)
