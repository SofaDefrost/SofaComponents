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

        
def MergeMeshes(attachedTo , name='MergeMeshes', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, nbMeshes=2, npoints=0, position=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), quads=array([], shape=(0, 4), dtype=int32), polygons=array([], shape=(0, 1), dtype=int32), tetrahedra=array([], shape=(0, 4), dtype=int32), hexahedra=array([], shape=(0, 8), dtype=int32), position1=array([], shape=(0, 3), dtype=float64), position2=array([], shape=(0, 3), dtype=float64), edges1=array([], shape=(0, 2), dtype=int32), edges2=array([], shape=(0, 2), dtype=int32), triangles1=array([], shape=(0, 3), dtype=int32), triangles2=array([], shape=(0, 3), dtype=int32), quads1=array([], shape=(0, 4), dtype=int32), quads2=array([], shape=(0, 4), dtype=int32), tetrahedra1=array([], shape=(0, 4), dtype=int32), tetrahedra2=array([], shape=(0, 4), dtype=int32), hexahedra1=array([], shape=(0, 8), dtype=int32), hexahedra2=array([], shape=(0, 8), dtype=int32), **kwargs):
    """Merge several meshes


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

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

		 position1: input positions for mesh 1

		 position2: input positions for mesh 2

		 edges1: input edges for mesh 1

		 edges2: input edges for mesh 2

		 triangles1: input triangles for mesh 1

		 triangles2: input triangles for mesh 2

		 quads1: input quads for mesh 1

		 quads2: input quads for mesh 2

		 tetrahedra1: input tetrahedra for mesh 1

		 tetrahedra2: input tetrahedra for mesh 2

		 hexahedra1: input hexahedra for mesh 1

		 hexahedra2: input hexahedra for mesh 2


    """
    return attachedTo.createObject("MergeMeshes" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, nbMeshes=nbMeshes, npoints=npoints, position=position, edges=edges, triangles=triangles, quads=quads, polygons=polygons, tetrahedra=tetrahedra, hexahedra=hexahedra, position1=position1, position2=position2, edges1=edges1, edges2=edges2, triangles1=triangles1, triangles2=triangles2, quads1=quads1, quads2=quads2, tetrahedra1=tetrahedra1, tetrahedra2=tetrahedra2, hexahedra1=hexahedra1, hexahedra2=hexahedra2, **kwargs)
