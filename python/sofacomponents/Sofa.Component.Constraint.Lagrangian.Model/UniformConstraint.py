# -*- coding: utf-8 -*-


"""
Component UniformConstraint

.. autofunction:: UniformConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def UniformConstraint(attachedTo , name='UniformConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, constraintIndex=0, endTime=-1.0, iterative=1, constrainToRestPos=0, **kwargs):
    """A constraint equation applied on all dofs.


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

		 iterative: Iterate over the bilateral constraints, otherwise a block factorisation is computed.

		 constrainToRestPos: if false, constrains the pos to be zero / if true constraint the current position to stay at rest position


    """
    return attachedTo.createObject("UniformConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, constraintIndex=constraintIndex, endTime=endTime, iterative=iterative, constrainToRestPos=constrainToRestPos, **kwargs)
