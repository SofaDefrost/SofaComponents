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

        
def BilateralInteractionConstraint(attachedTo , name='BilateralInteractionConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, group=0, constraintIndex=0, endTime=-1.0, first_point=[], second_point=[], rest_vector=[], numericalTolerance=0.0001, activateAtIteration=0, merge=0, derivative=0, keepOrientationDifference=0, **kwargs):
    """TODO-BilateralInteractionConstraint


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 constraintIndex: Constraint index (first index in the right hand term resolution vector)

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 first_point: index of the constraint on the first model

		 second_point: index of the constraint on the second model

		 rest_vector: Relative position to maintain between attached points (optional)

		 numericalTolerance: a real value specifying the tolerance during the constraint solving. (default=0.0001

		 activateAtIteration: activate constraint at specified interation (0 = always enabled, -1=disabled)

		 merge: TEST: merge the bilateral constraints in a unique constraint

		 derivative: TEST: derivative

		 keepOrientationDifference: keep the initial difference in orientation (only for rigids)


    """
    return attachedTo.createObject("BilateralInteractionConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, constraintIndex=constraintIndex, endTime=endTime, first_point=first_point, second_point=second_point, rest_vector=rest_vector, numericalTolerance=numericalTolerance, activateAtIteration=activateAtIteration, merge=merge, derivative=derivative, keepOrientationDifference=keepOrientationDifference, **kwargs)
