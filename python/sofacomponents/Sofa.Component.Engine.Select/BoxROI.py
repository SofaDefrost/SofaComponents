# -*- coding: utf-8 -*-


"""
Component BoxROI

.. autofunction:: BoxROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BoxROI(attachedTo , name='BoxROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, box=array([], shape=(0, 6), dtype=float64), orientedBox=array([], shape=(0, 10), dtype=float64), position=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), tetrahedra=array([], shape=(0, 4), dtype=int32), hexahedra=array([], shape=(0, 8), dtype=int32), quad=array([], shape=(0, 4), dtype=int32), computeEdges=1, computeTriangles=1, computeTetrahedra=1, computeHexahedra=1, computeQuad=1, strict=1, indices=array([], dtype=int32), edgeIndices=array([], dtype=int32), triangleIndices=array([], dtype=int32), tetrahedronIndices=array([], dtype=int32), hexahedronIndices=array([], dtype=int32), quadIndices=array([], dtype=int32), pointsInROI=array([], shape=(0, 3), dtype=float64), edgesInROI=array([], shape=(0, 2), dtype=int32), trianglesInROI=array([], shape=(0, 3), dtype=int32), tetrahedraInROI=array([], shape=(0, 4), dtype=int32), hexahedraInROI=array([], shape=(0, 8), dtype=int32), quadInROI=array([], shape=(0, 4), dtype=int32), nbIndices=0, drawBoxes=0, drawPoints=0, drawEdges=0, drawTriangles=0, drawTetrahedra=0, drawHexahedra=0, drawQuads=0, drawSize=1.0, doUpdate=1, **kwargs):
    """Find the primitives (vertex/edge/triangle/quad/tetrahedron/hexahedron) inside given boxes


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 box: List of boxes defined by xmin,ymin,zmin, xmax,ymax,zmax

		 orientedBox: List of boxes defined by 3 points (p0, p1, p2) and a depth distance 
A parallelogram will be defined by (p0, p1, p2, p3 = p0 + (p2-p1)). 
The box will finaly correspond to the parallelogram extrusion of depth/2 
along its normal and depth/2 in the opposite direction. 

		 position: Rest position coordinates of the degrees of freedom. 
If empty the positions from a MechanicalObject then a MeshLoader are searched in the current context. 
If none are found the parent's context is searched for MechanicalObject.

		 edges: Edge Topology

		 triangles: Triangle Topology

		 tetrahedra: Tetrahedron Topology

		 hexahedra: Hexahedron Topology

		 quad: Quad Topology

		 computeEdges: If true, will compute edge list and index list inside the ROI. (default = true)

		 computeTriangles: If true, will compute triangle list and index list inside the ROI. (default = true)

		 computeTetrahedra: If true, will compute tetrahedra list and index list inside the ROI. (default = true)

		 computeHexahedra: If true, will compute hexahedra list and index list inside the ROI. (default = true)

		 computeQuad: If true, will compute quad list and index list inside the ROI. (default = true)

		 strict: If true, an element is inside the box iif all of its nodes are inside. If False, only the center point of the element is checked. (default = true)

		 indices: Indices of the points contained in the ROI

		 edgeIndices: Indices of the edges contained in the ROI

		 triangleIndices: Indices of the triangles contained in the ROI

		 tetrahedronIndices: Indices of the tetrahedra contained in the ROI

		 hexahedronIndices: Indices of the hexahedra contained in the ROI

		 quadIndices: Indices of the quad contained in the ROI

		 pointsInROI: Points contained in the ROI

		 edgesInROI: Edges contained in the ROI

		 trianglesInROI: Triangles contained in the ROI

		 tetrahedraInROI: Tetrahedra contained in the ROI

		 hexahedraInROI: Hexahedra contained in the ROI

		 quadInROI: Quad contained in the ROI

		 nbIndices: Number of selected indices

		 drawBoxes: Draw Boxes. (default = false)

		 drawPoints: Draw Points. (default = false)

		 drawEdges: Draw Edges. (default = false)

		 drawTriangles: Draw Triangles. (default = false)

		 drawTetrahedra: Draw Tetrahedra. (default = false)

		 drawHexahedra: Draw Tetrahedra. (default = false)

		 drawQuads: Draw Quads. (default = false)

		 drawSize: rendering size for box and topological elements

		 doUpdate: If true, updates the selection at the beginning of simulation steps. (default = true)


    """
    return attachedTo.createObject("BoxROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, box=box, orientedBox=orientedBox, position=position, edges=edges, triangles=triangles, tetrahedra=tetrahedra, hexahedra=hexahedra, quad=quad, computeEdges=computeEdges, computeTriangles=computeTriangles, computeTetrahedra=computeTetrahedra, computeHexahedra=computeHexahedra, computeQuad=computeQuad, strict=strict, indices=indices, edgeIndices=edgeIndices, triangleIndices=triangleIndices, tetrahedronIndices=tetrahedronIndices, hexahedronIndices=hexahedronIndices, quadIndices=quadIndices, pointsInROI=pointsInROI, edgesInROI=edgesInROI, trianglesInROI=trianglesInROI, tetrahedraInROI=tetrahedraInROI, hexahedraInROI=hexahedraInROI, quadInROI=quadInROI, nbIndices=nbIndices, drawBoxes=drawBoxes, drawPoints=drawPoints, drawEdges=drawEdges, drawTriangles=drawTriangles, drawTetrahedra=drawTetrahedra, drawHexahedra=drawHexahedra, drawQuads=drawQuads, drawSize=drawSize, doUpdate=doUpdate, **kwargs)
