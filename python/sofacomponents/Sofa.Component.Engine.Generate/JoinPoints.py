# -*- coding: utf-8 -*-


"""
Component JoinPoints

.. autofunction:: JoinPoints

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def JoinPoints(attachedTo , name='JoinPoints', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, points=array([], shape=(0, 3), dtype=float64), distance=0.0, mergedPoints=array([], shape=(0, 3), dtype=float64), **kwargs):
    """?


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 points: Points

		 distance: Distance to merge points

		 mergedPoints: Merged Points


    """
    return attachedTo.createObject("JoinPoints" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, points=points, distance=distance, mergedPoints=mergedPoints, **kwargs)
