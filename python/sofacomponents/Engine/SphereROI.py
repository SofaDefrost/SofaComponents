# -*- coding: utf-8 -*-


"""
Component SphereROI

.. autofunction:: SphereROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SphereROI(attachedTo , name='SphereROI', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, centers=[], radii=[], direction=[[0.0, 0.0, 0.0]], normal=[[0.0, 0.0, 0.0]], edgeAngle=0.0, triAngle=0.0, position=[], edges=[], triangles=[], quads=[], tetrahedra=[], computeEdges=1, computeTriangles=1, computeQuads=1, computeTetrahedra=1, indices=[[0]], edgeIndices=[], triangleIndices=[], quadIndices=[], tetrahedronIndices=[], pointsInROI=[], edgesInROI=[], trianglesInROI=[], quadsInROI=[], tetrahedraInROI=[], indicesOut=[], drawSphere=0, drawPoints=0, drawEdges=0, drawTriangles=0, drawQuads=0, drawTetrahedra=0, drawSize=0.0, **kwargs):
    """Find the primitives (vertex/edge/triangle/tetrahedron) inside a given sphere


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 centers: Center(s) of the sphere(s)

		 radii: Radius(i) of the sphere(s)

		 direction: Edge direction(if edgeAngle > 0)

		 normal: Normal direction of the triangles (if triAngle > 0)

		 edgeAngle: Max angle between the direction of the selected edges and the specified direction

		 triAngle: Max angle between the normal of the selected triangle and the specified normal direction

		 position: Rest position coordinates of the degrees of freedom

		 edges: Edge Topology

		 triangles: Triangle Topology

		 quads: Quads Topology

		 tetrahedra: Tetrahedron Topology

		 computeEdges: If true, will compute edge list and index list inside the ROI.

		 computeTriangles: If true, will compute triangle list and index list inside the ROI.

		 computeQuads: If true, will compute quad list and index list inside the ROI.

		 computeTetrahedra: If true, will compute tetrahedra list and index list inside the ROI.

		 indices: Indices of the points contained in the ROI

		 edgeIndices: Indices of the edges contained in the ROI

		 triangleIndices: Indices of the triangles contained in the ROI

		 quadIndices: Indices of the quads contained in the ROI

		 tetrahedronIndices: Indices of the tetrahedra contained in the ROI

		 pointsInROI: Points contained in the ROI

		 edgesInROI: Edges contained in the ROI

		 trianglesInROI: Triangles contained in the ROI

		 quadsInROI: Quads contained in the ROI

		 tetrahedraInROI: Tetrahedra contained in the ROI

		 indicesOut: Indices of the points not contained in the ROI

		 drawSphere: Draw shpere(s)

		 drawPoints: Draw Points

		 drawEdges: Draw Edges

		 drawTriangles: Draw Triangles

		 drawQuads: Draw Quads

		 drawTetrahedra: Draw Tetrahedra

		 drawSize: rendering size for box and topological elements


    """
    return attachedTo.createObject("SphereROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, centers=centers, radii=radii, direction=direction, normal=normal, edgeAngle=edgeAngle, triAngle=triAngle, position=position, edges=edges, triangles=triangles, quads=quads, tetrahedra=tetrahedra, computeEdges=computeEdges, computeTriangles=computeTriangles, computeQuads=computeQuads, computeTetrahedra=computeTetrahedra, indices=indices, edgeIndices=edgeIndices, triangleIndices=triangleIndices, quadIndices=quadIndices, tetrahedronIndices=tetrahedronIndices, pointsInROI=pointsInROI, edgesInROI=edgesInROI, trianglesInROI=trianglesInROI, quadsInROI=quadsInROI, tetrahedraInROI=tetrahedraInROI, indicesOut=indicesOut, drawSphere=drawSphere, drawPoints=drawPoints, drawEdges=drawEdges, drawTriangles=drawTriangles, drawQuads=drawQuads, drawTetrahedra=drawTetrahedra, drawSize=drawSize, **kwargs)
