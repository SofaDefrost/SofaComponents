# -*- coding: utf-8 -*-


"""
Component FixedTranslationConstraint

.. autofunction:: FixedTranslationConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FixedTranslationConstraint(attachedTo , name='FixedTranslationConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, indices=array([0], dtype=int32), fixAll=0, drawSize=0.0, coordinates=array([], dtype=int32), **kwargs):
    """Attach given rigids to their initial positions but they still can have rotations


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

		 indices: Indices of the fixed points

		 fixAll: filter all the DOF to implement a fixed object

		 drawSize: 0 -> point based rendering, >0 -> radius of spheres

		 coordinates: Coordinates of the fixed points


    """
    return attachedTo.createObject("FixedTranslationConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, indices=indices, fixAll=fixAll, drawSize=drawSize, coordinates=coordinates, **kwargs)
