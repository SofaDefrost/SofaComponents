# -*- coding: utf-8 -*-


"""
Component PartialFixedConstraint

.. autofunction:: PartialFixedConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PartialFixedConstraint(attachedTo , name='PartialFixedConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, group=0, endTime=-1.0, indices=[[0]], fixAll=0, drawSize=0.0, fixedDirections=[[1, 1, 1]], activate_projectVelocity=0, **kwargs):
    """Attach given particles to their initial positions


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 indices: Indices of the fixed points

		 fixAll: filter all the DOF to implement a fixed object

		 drawSize: 0 -> point based rendering, >0 -> radius of spheres

		 fixedDirections: for each direction, 1 if fixed, 0 if free

		 activate_projectVelocity: activate project velocity to set velocity


    """
    return attachedTo.createObject("PartialFixedConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, endTime=endTime, indices=indices, fixAll=fixAll, drawSize=drawSize, fixedDirections=fixedDirections, activate_projectVelocity=activate_projectVelocity, **kwargs)
