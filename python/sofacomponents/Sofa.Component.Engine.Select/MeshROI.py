# -*- coding: utf-8 -*-


"""
Component MeshROI

.. autofunction:: MeshROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshROI(attachedTo , name='MeshROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), tetrahedra=array([], shape=(0, 4), dtype=int32), ROIposition=array([], shape=(0, 3), dtype=float64), ROIedges=array([], shape=(0, 2), dtype=int32), ROItriangles=array([], shape=(0, 3), dtype=int32), computeEdges=1, computeTriangles=1, computeTetrahedra=1, computeMeshROI=1, box=array([0., 0., 0., 0., 0., 0.]), indices=array([0], dtype=int32), edgeIndices=array([], dtype=int32), triangleIndices=array([], dtype=int32), tetrahedronIndices=array([], dtype=int32), pointsInROI=array([], shape=(0, 3), dtype=float64), edgesInROI=array([], shape=(0, 2), dtype=int32), trianglesInROI=array([], shape=(0, 3), dtype=int32), tetrahedraInROI=array([], shape=(0, 4), dtype=int32), pointsOutROI=array([], shape=(0, 3), dtype=float64), edgesOutROI=array([], shape=(0, 2), dtype=int32), trianglesOutROI=array([], shape=(0, 3), dtype=int32), tetrahedraOutROI=array([], shape=(0, 4), dtype=int32), indicesOut=array([], dtype=int32), edgeOutIndices=array([], dtype=int32), triangleOutIndices=array([], dtype=int32), tetrahedronOutIndices=array([], dtype=int32), drawOut=0, drawMesh=0, drawBox=0, drawPoints=0, drawEdges=0, drawTriangles=0, drawTetrahedra=0, drawSize=0.0, doUpdate=0, **kwargs):
    """Find the primitives (vertex/edge/triangle/tetrahedron) inside a given mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: Rest position coordinates of the degrees of freedom

		 edges: Edge Topology

		 triangles: Triangle Topology

		 tetrahedra: Tetrahedron Topology

		 ROIposition: ROI position coordinates of the degrees of freedom

		 ROIedges: ROI Edge Topology

		 ROItriangles: ROI Triangle Topology

		 computeEdges: If true, will compute edge list and index list inside the ROI.

		 computeTriangles: If true, will compute triangle list and index list inside the ROI.

		 computeTetrahedra: If true, will compute tetrahedra list and index list inside the ROI.

		 computeMeshROI: Compute with the mesh (not only bounding box)

		 box: Bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 indices: Indices of the points contained in the ROI

		 edgeIndices: Indices of the edges contained in the ROI

		 triangleIndices: Indices of the triangles contained in the ROI

		 tetrahedronIndices: Indices of the tetrahedra contained in the ROI

		 pointsInROI: Points contained in the ROI

		 edgesInROI: Edges contained in the ROI

		 trianglesInROI: Triangles contained in the ROI

		 tetrahedraInROI: Tetrahedra contained in the ROI

		 pointsOutROI: Points not contained in the ROI

		 edgesOutROI: Edges not contained in the ROI

		 trianglesOutROI: Triangles not contained in the ROI

		 tetrahedraOutROI: Tetrahedra not contained in the ROI

		 indicesOut: Indices of the points not contained in the ROI

		 edgeOutIndices: Indices of the edges not contained in the ROI

		 triangleOutIndices: Indices of the triangles not contained in the ROI

		 tetrahedronOutIndices: Indices of the tetrahedra not contained in the ROI

		 drawOut: Draw the data not contained in the ROI

		 drawMesh: Draw Mesh used for the ROI

		 drawBox: Draw the Bounding box around the mesh used for the ROI

		 drawPoints: Draw Points

		 drawEdges: Draw Edges

		 drawTriangles: Draw Triangles

		 drawTetrahedra: Draw Tetrahedra

		 drawSize: rendering size for mesh and topological elements

		 doUpdate: Update the computation (not only at the init)


    """
    return attachedTo.createObject("MeshROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, edges=edges, triangles=triangles, tetrahedra=tetrahedra, ROIposition=ROIposition, ROIedges=ROIedges, ROItriangles=ROItriangles, computeEdges=computeEdges, computeTriangles=computeTriangles, computeTetrahedra=computeTetrahedra, computeMeshROI=computeMeshROI, box=box, indices=indices, edgeIndices=edgeIndices, triangleIndices=triangleIndices, tetrahedronIndices=tetrahedronIndices, pointsInROI=pointsInROI, edgesInROI=edgesInROI, trianglesInROI=trianglesInROI, tetrahedraInROI=tetrahedraInROI, pointsOutROI=pointsOutROI, edgesOutROI=edgesOutROI, trianglesOutROI=trianglesOutROI, tetrahedraOutROI=tetrahedraOutROI, indicesOut=indicesOut, edgeOutIndices=edgeOutIndices, triangleOutIndices=triangleOutIndices, tetrahedronOutIndices=tetrahedronOutIndices, drawOut=drawOut, drawMesh=drawMesh, drawBox=drawBox, drawPoints=drawPoints, drawEdges=drawEdges, drawTriangles=drawTriangles, drawTetrahedra=drawTetrahedra, drawSize=drawSize, doUpdate=doUpdate, **kwargs)
