# -*- coding: utf-8 -*-


"""
Component PartialLinearMovementConstraint

.. autofunction:: PartialLinearMovementConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PartialLinearMovementConstraint(attachedTo , name='PartialLinearMovementConstraint', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, group=0, endTime=-1.0, indices=array([0], dtype=int32), keyTimes=array([0.]), movements=array([[0., 0., 0.]]), showMovement=0, linearMovementBetweenNodesInIndices=0, mainIndice=0, minDepIndice=0, maxDepIndice=0, imposedDisplacmentOnMacroNodes=array([], dtype=float64), X0=0.0, Y0=0.0, Z0=0.0, movedDirections=array([1, 1, 1], dtype=int8), **kwargs):
    """translate given particles


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

		 keyTimes: key times for the movements

		 movements: movements corresponding to the key times

		 showMovement: Visualization of the movement to be applied to constrained dofs.

		 linearMovementBetweenNodesInIndices: Take into account the linear movement between the constrained points

		 mainIndice: The main indice node in the list of constrained nodes, it defines how to apply the linear movement between this constrained nodes 

		 minDepIndice: The indice node in the list of constrained nodes, which is imposed the minimum displacment 

		 maxDepIndice: The indice node in the list of constrained nodes, which is imposed the maximum displacment 

		 imposedDisplacmentOnMacroNodes: The imposed displacment on macro nodes

		 X0: Size of specimen in X-direction

		 Y0: Size of specimen in Y-direction

		 Z0: Size of specimen in Z-direction

		 movedDirections: for each direction, 1 if moved, 0 if free


    """
    return attachedTo.createObject("PartialLinearMovementConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, group=group, endTime=endTime, indices=indices, keyTimes=keyTimes, movements=movements, showMovement=showMovement, linearMovementBetweenNodesInIndices=linearMovementBetweenNodesInIndices, mainIndice=mainIndice, minDepIndice=minDepIndice, maxDepIndice=maxDepIndice, imposedDisplacmentOnMacroNodes=imposedDisplacmentOnMacroNodes, X0=X0, Y0=Y0, Z0=Z0, movedDirections=movedDirections, **kwargs)
