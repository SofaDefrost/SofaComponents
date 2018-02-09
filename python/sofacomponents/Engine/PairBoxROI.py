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

        
def PairBoxROI(attachedTo , name='PairBoxROI', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inclusiveBox=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], includedBox=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], position=[], meshPosition=[], indices=[], pointsInROI=[], drawInclusiveBox=0, drawInclusdedBx=0, drawPoints=0, drawSize=0.0, **kwargs):
    """Find the primitives (vertex/edge/triangle/tetrahedron) inside a given box


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inclusiveBox: Inclusive box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 includedBox: Included box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 position: Rest position coordinates of the degrees of freedom

		 meshPosition: Vertices of the mesh loaded

		 indices: Indices of the points contained in the ROI

		 pointsInROI: Points contained in the ROI

		 drawInclusiveBox: Draw Inclusive Box

		 drawInclusdedBx: Draw Included Box

		 drawPoints: Draw Points

		 drawSize: Draw Size


    """
    return attachedTo.createObject("PairBoxROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inclusiveBox=inclusiveBox, includedBox=includedBox, position=position, meshPosition=meshPosition, indices=indices, pointsInROI=pointsInROI, drawInclusiveBox=drawInclusiveBox, drawInclusdedBx=drawInclusdedBx, drawPoints=drawPoints, drawSize=drawSize, **kwargs)
