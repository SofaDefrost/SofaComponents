# -*- coding: utf-8 -*-


"""
Component MeshSampler

.. autofunction:: MeshSampler

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshSampler(attachedTo , name='MeshSampler', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, number=1, position=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), maxIter=100, outputPosition=array([], shape=(0, 3), dtype=float64), **kwargs):
    """Select uniformly distributed points on a mesh based on Euclidean or Geodesic distance measure


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 number: Sample number

		 position: Input positions.

		 edges: Input edges for geodesic sampling (Euclidean distances are used if not specified).

		 maxIter: Max number of Lloyd iterations.

		 outputIndices: Computed sample indices.

		 outputPosition: Computed sample coordinates.


    """
    return attachedTo.createObject("MeshSampler" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, number=number, position=position, edges=edges, maxIter=maxIter, outputIndices=outputIndices, outputPosition=outputPosition, **kwargs)
