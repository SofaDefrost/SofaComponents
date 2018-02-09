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

        
def MeshSubsetEngine(attachedTo , name='MeshSubsetEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inputPosition=[], inputEdges=[], inputTriangles=[], inputQuads=[], indices=[], position=[], edges=[], triangles=[], quads=[], **kwargs):
    """Extract a mesh subset based on selected vertices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

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
    return attachedTo.createObject("MeshSubsetEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inputPosition=inputPosition, inputEdges=inputEdges, inputTriangles=inputTriangles, inputQuads=inputQuads, indices=indices, position=position, edges=edges, triangles=triangles, quads=quads, **kwargs)
