# -*- coding: utf-8 -*-


"""
Component ClusteringEngine

.. autofunction:: ClusteringEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ClusteringEngine(attachedTo , name='ClusteringEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, useTopo=1, radius=1.0, fixedRadius=1.0, number=-1, fixedPosition=array([], shape=(0, 3), dtype=float64), position=array([], shape=(0, 3), dtype=float64), cluster=array([], shape=(0, 1), dtype=int32), inFile='', outFile='', **kwargs):
    """Group points into overlapping clusters according to a user defined number of clusters and radius


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 useTopo: Use avalaible topology to compute neighborhood.

		 radius: Neighborhood range.

		 fixedRadius: Neighborhood range (for non mechanical particles).

		 number: Number of clusters (-1 means that all input points are selected).

		 fixedPosition: Input positions of fixed (non mechanical) particles.

		 position: Input rest positions.

		 cluster: Computed clusters.

		 inFile: import precomputed clusters

		 outFile: export clusters


    """
    return attachedTo.createObject("ClusteringEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, useTopo=useTopo, radius=radius, fixedRadius=fixedRadius, number=number, fixedPosition=fixedPosition, position=position, cluster=cluster, inFile=inFile, outFile=outFile, **kwargs)
