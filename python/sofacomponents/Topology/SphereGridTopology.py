# -*- coding: utf-8 -*-


"""
Component SphereGridTopology

.. autofunction:: SphereGridTopology

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SphereGridTopology(attachedTo , name='SphereGridTopology', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, fileTopology='', position=[], edges=[[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7], [0, 4], [1, 5], [2, 6], [3, 7]], triangles=[[0, 1, 3], [0, 3, 2], [4, 5, 7], [4, 7, 6], [0, 1, 5], [0, 5, 4], [2, 3, 7], [2, 7, 6], [0, 2, 6], [0, 6, 4], [1, 3, 7], [1, 7, 5]], quads=[[0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4], [2, 3, 7, 6], [0, 2, 6, 4], [1, 3, 7, 5]], tetrahedra=[], isToPrint=0, hexahedra=[[0, 1, 3, 2, 4, 5, 7, 6]], uv=[], drawEdges=0, drawTriangles=0, drawQuads=0, drawTetrahedra=0, drawHexahedra=0, n=[[2, 2, 2]], computeHexaList=1, computeQuadList=1, computeEdgeList=1, computePointList=1, createTexCoords=0, center=[[0.0, 0.0, 0.0]], axis=[[0.0, 0.0, 1.0]], radius=1.0, **kwargs):
    """Sphere grid in 3D


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 fileTopology: Filename of the mesh

		 position: List of point positions

		 edges: List of edge indices

		 triangles: List of triangle indices

		 quads: List of quad indices

		 tetrahedra: List of tetrahedron indices

		 isToPrint: suppress somes data before using save as function

		 hexahedra: List of hexahedron indices

		 uv: List of uv coordinates

		 drawEdges: if true, draw the topology Edges

		 drawTriangles: if true, draw the topology Triangles

		 drawQuads: if true, draw the topology Quads

		 drawTetrahedra: if true, draw the topology Tetrahedra

		 drawHexahedra: if true, draw the topology hexahedra

		 n: grid resolution. (default = 2 2 2)

		 computeHexaList: put true if the list of Hexahedra is needed during init (default=true)

		 computeQuadList: put true if the list of Quad is needed during init (default=true)

		 computeEdgeList: put true if the list of Lines is needed during init (default=true)

		 computePointList: put true if the list of Points is needed during init (default=true)

		 createTexCoords: If set to true, virtual texture coordinates will be generated using 3D interpolation (default=false).

		 center: Center of the cylinder

		 axis: Main direction of the cylinder

		 radius: Radius of the cylinder


    """
    return attachedTo.createObject("SphereGridTopology" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, fileTopology=fileTopology, position=position, edges=edges, triangles=triangles, quads=quads, tetrahedra=tetrahedra, isToPrint=isToPrint, hexahedra=hexahedra, uv=uv, drawEdges=drawEdges, drawTriangles=drawTriangles, drawQuads=drawQuads, drawTetrahedra=drawTetrahedra, drawHexahedra=drawHexahedra, n=n, computeHexaList=computeHexaList, computeQuadList=computeQuadList, computeEdgeList=computeEdgeList, computePointList=computePointList, createTexCoords=createTexCoords, center=center, axis=axis, radius=radius, **kwargs)
