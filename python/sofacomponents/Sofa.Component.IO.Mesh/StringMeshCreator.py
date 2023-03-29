# -*- coding: utf-8 -*-


"""
Component StringMeshCreator

.. autofunction:: StringMeshCreator

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def StringMeshCreator(attachedTo , name='StringMeshCreator', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, filename='', position=array([], shape=(0, 3), dtype=float64), polylines=array([], shape=(0, 1), dtype=int32), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), quads=array([], shape=(0, 4), dtype=int32), polygons=array([], shape=(0, 1), dtype=int32), highOrderEdgePositions=array([], shape=(0, 4), dtype=int32), highOrderTrianglePositions=array([], shape=(0, 5), dtype=int32), highOrderQuadPositions=array([], shape=(0, 6), dtype=int32), tetrahedra=array([], shape=(0, 4), dtype=int32), hexahedra=array([], shape=(0, 8), dtype=int32), pentahedra=array([], shape=(0, 6), dtype=int32), highOrderTetrahedronPositions=array([], shape=(0, 6), dtype=int32), highOrderHexahedronPositions=array([], shape=(0, 8), dtype=int32), pyramids=array([], shape=(0, 5), dtype=int32), normals=array([], shape=(0, 3), dtype=float64), edgesGroups=[], trianglesGroups=[], quadsGroups=[], polygonsGroups=[], tetrahedraGroups=[], hexahedraGroups=[], pentahedraGroups=[], pyramidsGroups=[], flipNormals=0, triangulate=0, createSubelements=0, onlyAttachedPoints=0, translation=array([0., 0., 0.]), rotation=array([0., 0., 0.]), scale3d=array([1., 1., 1.]), transformation=array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]]), resolution=2, **kwargs):
    """Procedural creation of a one-dimensional mesh.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 filename: Filename of the object

		 position: Vertices of the mesh loaded

		 polylines: Polylines of the mesh loaded

		 edges: Edges of the mesh loaded

		 triangles: Triangles of the mesh loaded

		 quads: Quads of the mesh loaded

		 polygons: Polygons of the mesh loaded

		 highOrderEdgePositions: High order edge points of the mesh loaded

		 highOrderTrianglePositions: High order triangle points of the mesh loaded

		 highOrderQuadPositions: High order quad points of the mesh loaded

		 tetrahedra: Tetrahedra of the mesh loaded

		 hexahedra: Hexahedra of the mesh loaded

		 pentahedra: Pentahedra of the mesh loaded

		 highOrderTetrahedronPositions: High order tetrahedron points of the mesh loaded

		 highOrderHexahedronPositions: High order hexahedron points of the mesh loaded

		 pyramids: Pyramids of the mesh loaded

		 normals: Normals of the mesh loaded

		 edgesGroups: Groups of Edges

		 trianglesGroups: Groups of Triangles

		 quadsGroups: Groups of Quads

		 polygonsGroups: Groups of Polygons

		 tetrahedraGroups: Groups of Tetrahedra

		 hexahedraGroups: Groups of Hexahedra

		 pentahedraGroups: Groups of Pentahedra

		 pyramidsGroups: Groups of Pyramids

		 flipNormals: Flip Normals

		 triangulate: Divide all polygons into triangles

		 createSubelements: Divide all n-D elements into their (n-1)-D boundary elements (e.g. tetrahedra to triangles)

		 onlyAttachedPoints: Only keep points attached to elements of the mesh

		 translation: Translation of the DOFs

		 rotation: Rotation of the DOFs

		 scale3d: Scale of the DOFs in 3 dimensions

		 transformation: 4x4 Homogeneous matrix to transform the DOFs (when present replace any)

		 resolution: Number of vertices


    """
    return attachedTo.createObject("StringMeshCreator" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, position=position, polylines=polylines, edges=edges, triangles=triangles, quads=quads, polygons=polygons, highOrderEdgePositions=highOrderEdgePositions, highOrderTrianglePositions=highOrderTrianglePositions, highOrderQuadPositions=highOrderQuadPositions, tetrahedra=tetrahedra, hexahedra=hexahedra, pentahedra=pentahedra, highOrderTetrahedronPositions=highOrderTetrahedronPositions, highOrderHexahedronPositions=highOrderHexahedronPositions, pyramids=pyramids, normals=normals, edgesGroups=edgesGroups, trianglesGroups=trianglesGroups, quadsGroups=quadsGroups, polygonsGroups=polygonsGroups, tetrahedraGroups=tetrahedraGroups, hexahedraGroups=hexahedraGroups, pentahedraGroups=pentahedraGroups, pyramidsGroups=pyramidsGroups, flipNormals=flipNormals, triangulate=triangulate, createSubelements=createSubelements, onlyAttachedPoints=onlyAttachedPoints, translation=translation, rotation=rotation, scale3d=scale3d, transformation=transformation, resolution=resolution, **kwargs)
