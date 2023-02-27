# -*- coding: utf-8 -*-


"""
Component PlaneROI

.. autofunction:: PlaneROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PlaneROI(attachedTo , name='PlaneROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, plane=array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]), position=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), tetrahedra=array([], shape=(0, 4), dtype=int32), computeEdges=1, computeTriangles=1, computeTetrahedra=1, indices=array([], dtype=int32), edgeIndices=array([], dtype=int32), triangleIndices=array([], dtype=int32), tetrahedronIndices=array([], dtype=int32), pointsInROI=array([], shape=(0, 3), dtype=float64), edgesInROI=array([], shape=(0, 2), dtype=int32), trianglesInROI=array([], shape=(0, 3), dtype=int32), tetrahedraInROI=array([], shape=(0, 4), dtype=int32), drawBoxes=0, drawPoints=0, drawEdges=0, drawTriangles=0, drawTetrahedra=0, drawSize=1.0, **kwargs):
    """Find the primitives inside a given plane


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 plane: Plane defined by 3 points and a depth distance

		 position: Rest position coordinates of the degrees of freedom

		 edges: Edge Topology

		 triangles: Triangle Topology

		 tetrahedra: Tetrahedron Topology

		 computeEdges: If true, will compute edge list and index list inside the ROI.

		 computeTriangles: If true, will compute triangle list and index list inside the ROI.

		 computeTetrahedra: If true, will compute tetrahedra list and index list inside the ROI.

		 indices: Indices of the points contained in the ROI

		 edgeIndices: Indices of the edges contained in the ROI

		 triangleIndices: Indices of the triangles contained in the ROI

		 tetrahedronIndices: Indices of the tetrahedra contained in the ROI

		 pointsInROI: Points contained in the ROI

		 edgesInROI: Edges contained in the ROI

		 trianglesInROI: Triangles contained in the ROI

		 tetrahedraInROI: Tetrahedra contained in the ROI

		 drawBoxes: Draw Box(es)

		 drawPoints: Draw Points

		 drawEdges: Draw Edges

		 drawTriangles: Draw Triangles

		 drawTetrahedra: Draw Tetrahedra

		 drawSize: rendering size for box and topological elements


    """
    return attachedTo.createObject("PlaneROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, plane=plane, position=position, edges=edges, triangles=triangles, tetrahedra=tetrahedra, computeEdges=computeEdges, computeTriangles=computeTriangles, computeTetrahedra=computeTetrahedra, indices=indices, edgeIndices=edgeIndices, triangleIndices=triangleIndices, tetrahedronIndices=tetrahedronIndices, pointsInROI=pointsInROI, edgesInROI=edgesInROI, trianglesInROI=trianglesInROI, tetrahedraInROI=tetrahedraInROI, drawBoxes=drawBoxes, drawPoints=drawPoints, drawEdges=drawEdges, drawTriangles=drawTriangles, drawTetrahedra=drawTetrahedra, drawSize=drawSize, **kwargs)
