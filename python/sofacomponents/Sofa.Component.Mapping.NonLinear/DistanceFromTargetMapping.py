# -*- coding: utf-8 -*-


"""
Component DistanceFromTargetMapping

.. autofunction:: DistanceFromTargetMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DistanceFromTargetMapping(attachedTo , name='DistanceFromTargetMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, indices=array([], dtype=int32), targetPositions=array([], shape=(0, 3), dtype=float64), restLengths=array([], dtype=float64), geometricStiffness=2, showObjectScale=0.0, showColor=array([1., 1., 0., 1.], dtype=float32), **kwargs):
    """Compute edge extensions


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 mapForces: Are forces mapped ?

		 mapConstraints: Are constraints mapped ?

		 mapMasses: Are masses mapped ?

		 mapMatrices: Are matrix explicit mapped?

		 applyRestPosition: set to true to apply this mapping to restPosition at init

		 indices: Indices of the parent points

		 targetPositions: Positions to compute the distances from

		 restLengths: Rest lengths of the connections.

		 geometricStiffness: 0 -> no GS, 1 -> exact GS, 2 -> stabilized GS (default)

		 showObjectScale: Scale for object display

		 showColor: Color for object display. (default=[1.0,1.0,0.0,1.0])


    """
    return attachedTo.createObject("DistanceFromTargetMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, indices=indices, targetPositions=targetPositions, restLengths=restLengths, geometricStiffness=geometricStiffness, showObjectScale=showObjectScale, showColor=showColor, **kwargs)
