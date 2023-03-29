# -*- coding: utf-8 -*-


"""
Component PairBoxROI

.. autofunction:: PairBoxROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PairBoxROI(attachedTo , name='PairBoxROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, inclusiveBox=array([0., 0., 0., 0., 0., 0.]), includedBox=array([0., 0., 0., 0., 0., 0.]), position=array([], shape=(0, 3), dtype=float64), meshPosition=array([], shape=(0, 3), dtype=float64), indices=array([], dtype=int32), pointsInROI=array([], shape=(0, 3), dtype=float64), drawInclusiveBox=0, drawIncludedBox=0, drawPoints=0, drawSize=0.0, **kwargs):
    """Find the primitives (vertex/edge/triangle/tetrahedron) inside a given box


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 inclusiveBox: Inclusive box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 includedBox: Included box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 position: Rest position coordinates of the degrees of freedom

		 meshPosition: Vertices of the mesh loaded

		 indices: Indices of the points contained in the ROI

		 pointsInROI: Points contained in the ROI

		 drawInclusiveBox: Draw Inclusive Box

		 drawIncludedBox: Draw Included Box

		 drawPoints: Draw Points

		 drawSize: Draw Size


    """
    return attachedTo.createObject("PairBoxROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, inclusiveBox=inclusiveBox, includedBox=includedBox, position=position, meshPosition=meshPosition, indices=indices, pointsInROI=pointsInROI, drawInclusiveBox=drawInclusiveBox, drawIncludedBox=drawIncludedBox, drawPoints=drawPoints, drawSize=drawSize, **kwargs)
