# -*- coding: utf-8 -*-


"""
Component MeshClosingEngine

.. autofunction:: MeshClosingEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshClosingEngine(attachedTo , name='MeshClosingEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inputPosition=[], inputTriangles=[], inputQuads=[], position=[], triangles=[], quads=[], indices='', closingPosition=[], closingTriangles=[], **kwargs):
    """Merge several meshes


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inputPosition: input vertices

		 inputTriangles: input triangles

		 inputQuads: input quads

		 position: Vertices of closed mesh

		 triangles: Triangles of closed mesh

		 quads: Quads of closed mesh (=input quads with current method)

		 indices: Index lists of the closing parts

		 closingPosition: Vertices of the closing parts

		 closingTriangles: Triangles of the closing parts


    """
    return attachedTo.createObject("MeshClosingEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inputPosition=inputPosition, inputTriangles=inputTriangles, inputQuads=inputQuads, position=position, triangles=triangles, quads=quads, indices=indices, closingPosition=closingPosition, closingTriangles=closingTriangles, **kwargs)
