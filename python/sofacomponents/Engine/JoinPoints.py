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

        
def JoinPoints(attachedTo , name='JoinPoints', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, points=[], distance=0.0, mergedPoints=[], **kwargs):
    """?


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 points: Points

		 distance: Distance to merge points

		 mergedPoints: Merged Points


    """
    return attachedTo.createObject("JoinPoints" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, points=points, distance=distance, mergedPoints=mergedPoints, **kwargs)
