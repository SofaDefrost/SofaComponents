# -*- coding: utf-8 -*-


"""
Component AttachConstraint

.. autofunction:: AttachConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AttachConstraint(attachedTo , name='AttachConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, indices1=array([], dtype=int32), indices2=array([], dtype=int32), twoWay=0, freeRotations=0, lastFreeRotation=0, restRotations=0, lastPos=array([0., 0., 0.]), lastDir=array([0., 0., 0.]), clamp=0, minDistance=-1.0, positionFactor=1.0, velocityFactor=1.0, responseFactor=1.0, constraintFactor=array([], dtype=float64), **kwargs):
    """Attach given pair of particles, projecting the positions of the second particles to the first ones


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

		 indices1: Indices of the source points on the first model

		 indices2: Indices of the fixed points on the second model

		 twoWay: true if forces should be projected back from model2 to model1

		 freeRotations: true to keep rotations free (only used for Rigid DOFs)

		 lastFreeRotation: true to keep rotation of the last attached point free (only used for Rigid DOFs)

		 restRotations: true to use rest rotations local offsets (only used for Rigid DOFs)

		 lastPos: position at which the attach constraint should become inactive

		 lastDir: direction from lastPos at which the attach coustraint should become inactive

		 clamp: true to clamp particles at lastPos instead of freeing them.

		 minDistance: the constraint become inactive if the distance between the points attached is bigger than minDistance.

		 positionFactor: IN: Factor applied to projection of position

		 velocityFactor: IN: Factor applied to projection of velocity

		 responseFactor: IN: Factor applied to projection of force/acceleration

		 constraintFactor: Constraint factor per pair of points constrained. 0 -> the constraint is released. 1 -> the constraint is fully constrained


    """
    return attachedTo.createObject("AttachConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, indices1=indices1, indices2=indices2, twoWay=twoWay, freeRotations=freeRotations, lastFreeRotation=lastFreeRotation, restRotations=restRotations, lastPos=lastPos, lastDir=lastDir, clamp=clamp, minDistance=minDistance, positionFactor=positionFactor, velocityFactor=velocityFactor, responseFactor=responseFactor, constraintFactor=constraintFactor, **kwargs)
