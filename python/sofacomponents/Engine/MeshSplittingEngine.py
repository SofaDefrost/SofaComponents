# -*- coding: utf-8 -*-


"""
Component MeshSplittingEngine

.. autofunction:: MeshSplittingEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshSplittingEngine(attachedTo , name='MeshSplittingEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[], edges=[], triangles=[], quads=[], tetrahedra=[], hexahedra=[], nbInputs=0, indexPairs=[], position1=[], **kwargs):
    """This class breaks a mesh in multiple parts, based on selected vertices or cells.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: input vertices

		 edges: input edges

		 triangles: input triangles

		 quads: input quads

		 tetrahedra: input tetrahedra

		 hexahedra: input hexahedra

		 nbInputs: Number of input vectors

		 indexPairs: couples for input vertices: ROI index + index in the ROI


    """
    return attachedTo.createObject("MeshSplittingEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, edges=edges, triangles=triangles, quads=quads, tetrahedra=tetrahedra, hexahedra=hexahedra, nbInputs=nbInputs, indexPairs=indexPairs, position1=position1, **kwargs)
