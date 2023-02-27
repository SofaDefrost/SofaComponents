# -*- coding: utf-8 -*-


"""
Component ProximityROI

.. autofunction:: ProximityROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ProximityROI(attachedTo , name='ProximityROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, centers=array([], shape=(0, 3), dtype=float64), radii=array([], dtype=float64), N=0, position=array([], shape=(0, 3), dtype=float64), indices=array([0], dtype=int32), pointsInROI=array([], shape=(0, 3), dtype=float64), distance=array([], dtype=float64), indicesOut=array([], dtype=int32), drawSphere=0, drawPoints=0, drawSize=1.0, **kwargs):
    """Find the N closest primitives from a given position


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 centers: Center(s) of the sphere(s)

		 radii: Radius(i) of the sphere(s)

		 N: Maximum number of points to select

		 position: Rest position coordinates of the degrees of freedom

		 indices: Indices of the points contained in the ROI

		 pointsInROI: Points contained in the ROI

		 distance: distance between the points contained in the ROI and the closest center.

		 indicesOut: Indices of the points not contained in the ROI

		 drawSphere: Draw shpere(s)

		 drawPoints: Draw Points

		 drawSize: rendering size for box and topological elements


    """
    return attachedTo.createObject("ProximityROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, centers=centers, radii=radii, N=N, position=position, indices=indices, pointsInROI=pointsInROI, distance=distance, indicesOut=indicesOut, drawSphere=drawSphere, drawPoints=drawPoints, drawSize=drawSize, **kwargs)
