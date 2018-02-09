# -*- coding: utf-8 -*-


"""
Component MergeMeshes

.. autofunction:: MergeMeshes

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MergeMeshes(attachedTo , name='MergeMeshes', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, nbMeshes=2, npoints=0, position=[], edges=[], triangles=[], quads=[], polygons=[], tetrahedra=[], hexahedra=[], position1=[], position2=[], edges1=[], edges2=[], triangles1=[], triangles2=[], quads1=[], quads2=[], tetrahedra1=[], tetrahedra2=[], hexahedra1=[], hexahedra2=[], **kwargs):
    """Merge several meshes


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 nbMeshes: number of meshes to merge

		 npoints: Number Of out points

		 position: Output Vertices of the merged mesh

		 edges: Output Edges of the merged mesh

		 triangles: Output Triangles of the merged mesh

		 quads: Output Quads of the merged mesh

		 polygons: Output Polygons of the merged mesh

		 tetrahedra: Output Tetrahedra of the merged mesh

		 hexahedra: Output Hexahedra of the merged mesh

		 position1: (No help available)

		 position2: (No help available)

		 edges1: (No help available)

		 edges2: (No help available)

		 triangles1: (No help available)

		 triangles2: (No help available)

		 quads1: (No help available)

		 quads2: (No help available)

		 tetrahedra1: (No help available)

		 tetrahedra2: (No help available)

		 hexahedra1: (No help available)

		 hexahedra2: (No help available)


    """
    return attachedTo.createObject("MergeMeshes" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, nbMeshes=nbMeshes, npoints=npoints, position=position, edges=edges, triangles=triangles, quads=quads, polygons=polygons, tetrahedra=tetrahedra, hexahedra=hexahedra, position1=position1, position2=position2, edges1=edges1, edges2=edges2, triangles1=triangles1, triangles2=triangles2, quads1=quads1, quads2=quads2, tetrahedra1=tetrahedra1, tetrahedra2=tetrahedra2, hexahedra1=hexahedra1, hexahedra2=hexahedra2, **kwargs)
