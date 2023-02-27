# -*- coding: utf-8 -*-


"""
Component MeshSubsetEngine

.. autofunction:: MeshSubsetEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshSubsetEngine(attachedTo , name='MeshSubsetEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, inputPosition=array([], shape=(0, 3), dtype=float64), inputEdges=array([], shape=(0, 2), dtype=int32), inputTriangles=array([], shape=(0, 3), dtype=int32), inputQuads=array([], shape=(0, 4), dtype=int32), indices=array([], dtype=int32), position=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), quads=array([], shape=(0, 4), dtype=int32), **kwargs):
    """Extract a mesh subset based on selected vertices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 inputPosition: input vertices

		 inputEdges: input edges

		 inputTriangles: input triangles

		 inputQuads: input quads

		 indices: Index lists of the selected vertices

		 position: Vertices of mesh subset

		 edges: edges of mesh subset

		 triangles: Triangles of mesh subset

		 quads: Quads of mesh subset


    """
    return attachedTo.createObject("MeshSubsetEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, inputPosition=inputPosition, inputEdges=inputEdges, inputTriangles=inputTriangles, inputQuads=inputQuads, indices=indices, position=position, edges=edges, triangles=triangles, quads=quads, **kwargs)
