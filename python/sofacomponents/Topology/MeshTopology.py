# -*- coding: utf-8 -*-


"""
Component MeshTopology

.. autofunction:: MeshTopology

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshTopology(attachedTo , name='MeshTopology', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, fileTopology='', position=[], edges=[], triangles=[], quads=[], tetrahedra=[], isToPrint=0, hexahedra=[], uv=[], drawEdges=0, drawTriangles=0, drawQuads=0, drawTetrahedra=0, drawHexahedra=0, **kwargs):
    """Generic mesh topology


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


    """
    return attachedTo.createObject("MeshTopology" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, fileTopology=fileTopology, position=position, edges=edges, triangles=triangles, quads=quads, tetrahedra=tetrahedra, isToPrint=isToPrint, hexahedra=hexahedra, uv=uv, drawEdges=drawEdges, drawTriangles=drawTriangles, drawQuads=drawQuads, drawTetrahedra=drawTetrahedra, drawHexahedra=drawHexahedra, **kwargs)
