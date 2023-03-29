# -*- coding: utf-8 -*-


"""
Component NearestPointROI

.. autofunction:: NearestPointROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NearestPointROI(attachedTo , name='NearestPointROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, inputIndices1=array([], dtype=int32), inputIndices2=array([], dtype=int32), radius=1.0, useRestPosition=1, indices1=array([], dtype=int32), indices2=array([], dtype=int32), edges=array([], shape=(0, 2), dtype=int32), indexPairs=array([], dtype=int32), distances=array([], dtype=float64), **kwargs):
    """Attach given pair of particles, projecting the positions of the second particles to the first ones


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 inputIndices1: Indices of the points to consider on the first model

		 inputIndices2: Indices of the points to consider on the first model

		 radius: Radius to search corresponding fixed point

		 useRestPosition: If true will use restPosition only at init

		 indices1: Indices from the first model associated to a dof from the second model

		 indices2: Indices from the second model associated to a dof from the first model

		 edges: List of edge indices

		 indexPairs: list of couples (parent index + index in the parent)

		 distances: List of distances between pairs of points


    """
    return attachedTo.createObject("NearestPointROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, inputIndices1=inputIndices1, inputIndices2=inputIndices2, radius=radius, useRestPosition=useRestPosition, indices1=indices1, indices2=indices2, edges=edges, indexPairs=indexPairs, distances=distances, **kwargs)
