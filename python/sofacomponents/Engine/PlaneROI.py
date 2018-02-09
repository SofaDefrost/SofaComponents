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

        
def PlaneROI(attachedTo , name='PlaneROI', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, plane=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], position=[], edges=[], triangles=[], tetrahedra=[], computeEdges=1, computeTriangles=1, computeTetrahedra=1, indices=[[0]], edgeIndices=[], triangleIndices=[], tetrahedronIndices=[], pointsInROI=[], edgesInROI=[], trianglesInROI=[], tetrahedraInROI=[], drawBoxes=0, drawPoints=0, drawEdges=0, drawTriangles=0, drawTetrahedra=0, drawSize=0.0, **kwargs):
    """Find the primitives inside a given plane


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

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
    return attachedTo.createObject("PlaneROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, plane=plane, position=position, edges=edges, triangles=triangles, tetrahedra=tetrahedra, computeEdges=computeEdges, computeTriangles=computeTriangles, computeTetrahedra=computeTetrahedra, indices=indices, edgeIndices=edgeIndices, triangleIndices=triangleIndices, tetrahedronIndices=tetrahedronIndices, pointsInROI=pointsInROI, edgesInROI=edgesInROI, trianglesInROI=trianglesInROI, tetrahedraInROI=tetrahedraInROI, drawBoxes=drawBoxes, drawPoints=drawPoints, drawEdges=drawEdges, drawTriangles=drawTriangles, drawTetrahedra=drawTetrahedra, drawSize=drawSize, **kwargs)
