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

        
def MeshSplittingEngine(attachedTo , name='MeshSplittingEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), quads=array([], shape=(0, 4), dtype=int32), tetrahedra=array([], shape=(0, 4), dtype=int32), hexahedra=array([], shape=(0, 8), dtype=int32), nbInputs=0, indexPairs=array([], dtype=int32), position1=array([], shape=(0, 3), dtype=float64), **kwargs):
    """This class breaks a mesh in multiple parts, based on selected vertices or cells.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: input vertices

		 edges: input edges

		 triangles: input triangles

		 quads: input quads

		 tetrahedra: input tetrahedra

		 hexahedra: input hexahedra

		 nbInputs: Number of input vectors

		 indexPairs: couples for input vertices: ROI index + index in the ROI

		 position1: output vertices(1)


    """
    return attachedTo.createObject("MeshSplittingEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, edges=edges, triangles=triangles, quads=quads, tetrahedra=tetrahedra, hexahedra=hexahedra, nbInputs=nbInputs, indexPairs=indexPairs, position1=position1, **kwargs)
