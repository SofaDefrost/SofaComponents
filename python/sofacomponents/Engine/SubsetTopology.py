# -*- coding: utf-8 -*-


"""
Component SubsetTopology

.. autofunction:: SubsetTopology

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SubsetTopology(attachedTo , name='SubsetTopology', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, box=[[0.0, 0.0, 0.0, 1.0, 1.0, 1.0]], centers=[], radii=[], direction=[[0.0, 0.0, 0.0]], normal=[[0.0, 0.0, 0.0]], edgeAngle=0.0, triAngle=0.0, rest_position=[], edges=[], triangles=[], quads=[], tetrahedra=[], hexahedra=[], tetrahedraInput=[], indices=[[0]], edgeIndices=[], triangleIndices=[], quadIndices=[], tetrahedronIndices=[], hexahedronIndices=[], pointsInROI=[], pointsOutROI=[], edgesInROI=[], edgesOutROI=[], trianglesInROI=[], trianglesOutROI=[], quadsInROI=[], quadsOutROI=[], tetrahedraInROI=[], tetrahedraOutROI=[], hexahedraInROI=[], hexahedraOutROI=[], nbrborder=0, localIndices=0, drawROI=0, drawPoints=0, drawEdges=0, drawTriangle=0, drawTetrahedra=0, drawSize=0.0, **kwargs):
    """Engine used to create subset topology given box, sphere, plan, ...


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 box: Box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 centers: Center(s) of the sphere(s)

		 radii: Radius(i) of the sphere(s)

		 direction: Edge direction(if edgeAngle > 0)

		 normal: Normal direction of the triangles (if triAngle > 0)

		 edgeAngle: Max angle between the direction of the selected edges and the specified direction

		 triAngle: Max angle between the normal of the selected triangle and the specified normal direction

		 rest_position: Rest position coordinates of the degrees of freedom

		 edges: Edge Topology

		 triangles: Triangle Topology

		 quads: Quad Topology

		 tetrahedra: Tetrahedron Topology

		 hexahedra: Hexahedron Topology

		 tetrahedraInput: Indices of the tetrahedra to keep

		 indices: Indices of the points contained in the ROI

		 edgeIndices: Indices of the edges contained in the ROI

		 triangleIndices: Indices of the triangles contained in the ROI

		 quadIndices: Indices of the quads contained in the ROI

		 tetrahedronIndices: Indices of the tetrahedra contained in the ROI

		 hexahedronIndices: Indices of the hexahedra contained in the ROI

		 pointsInROI: Points contained in the ROI

		 pointsOutROI: Points out of the ROI

		 edgesInROI: Edges contained in the ROI

		 edgesOutROI: Edges out of the ROI

		 trianglesInROI: Triangles contained in the ROI

		 trianglesOutROI: Triangles out of the ROI

		 quadsInROI: Quads contained in the ROI

		 quadsOutROI: Quads out of the ROI

		 tetrahedraInROI: Tetrahedra contained in the ROI

		 tetrahedraOutROI: Tetrahedra out of the ROI

		 hexahedraInROI: Hexahedra contained in the ROI

		 hexahedraOutROI: Hexahedra out of the ROI

		 nbrborder: If localIndices option is activated, will give the number of vertices on the border of the ROI (being the n first points of each output Topology). 

		 localIndices: If true, will compute local dof indices in topological elements

		 drawROI: Draw ROI

		 drawPoints: Draw Points

		 drawEdges: Draw Edges

		 drawTriangle: Draw Triangles

		 drawTetrahedra: Draw Tetrahedra

		 drawSize: rendering size for box and topological elements


    """
    return attachedTo.createObject("SubsetTopology" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, box=box, centers=centers, radii=radii, direction=direction, normal=normal, edgeAngle=edgeAngle, triAngle=triAngle, rest_position=rest_position, edges=edges, triangles=triangles, quads=quads, tetrahedra=tetrahedra, hexahedra=hexahedra, tetrahedraInput=tetrahedraInput, indices=indices, edgeIndices=edgeIndices, triangleIndices=triangleIndices, quadIndices=quadIndices, tetrahedronIndices=tetrahedronIndices, hexahedronIndices=hexahedronIndices, pointsInROI=pointsInROI, pointsOutROI=pointsOutROI, edgesInROI=edgesInROI, edgesOutROI=edgesOutROI, trianglesInROI=trianglesInROI, trianglesOutROI=trianglesOutROI, quadsInROI=quadsInROI, quadsOutROI=quadsOutROI, tetrahedraInROI=tetrahedraInROI, tetrahedraOutROI=tetrahedraOutROI, hexahedraInROI=hexahedraInROI, hexahedraOutROI=hexahedraOutROI, nbrborder=nbrborder, localIndices=localIndices, drawROI=drawROI, drawPoints=drawPoints, drawEdges=drawEdges, drawTriangle=drawTriangle, drawTetrahedra=drawTetrahedra, drawSize=drawSize, **kwargs)
