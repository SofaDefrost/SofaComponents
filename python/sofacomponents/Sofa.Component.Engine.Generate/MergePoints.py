# -*- coding: utf-8 -*-


"""
Component MergePoints

.. autofunction:: MergePoints

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MergePoints(attachedTo , name='MergePoints', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position1=array([], shape=(0, 3), dtype=float64), position2=array([], shape=(0, 3), dtype=float64), mappingX2=array([], dtype=int32), indices1=array([], dtype=int32), indices2=array([], dtype=int32), points=array([], shape=(0, 3), dtype=float64), noUpdate=0, **kwargs):
    """Merge 2 cordinate vectors


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position1: position coordinates of the degrees of freedom of the first object

		 position2: Rest position coordinates of the degrees of freedom of the second object

		 mappingX2: Mapping of indices to inject position2 inside position1 vertex buffer

		 indices1: Indices of the points of the first object

		 indices2: Indices of the points of the second object

		 points: position coordinates of the merge

		 noUpdate: do not update the output at eacth time step (false)


    """
    return attachedTo.createObject("MergePoints" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position1=position1, position2=position2, mappingX2=mappingX2, indices1=indices1, indices2=indices2, points=points, noUpdate=noUpdate, **kwargs)
