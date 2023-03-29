# -*- coding: utf-8 -*-


"""
Component ComplementaryROI

.. autofunction:: ComplementaryROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ComplementaryROI(attachedTo , name='ComplementaryROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), nbSet=0, indices=array([], dtype=int32), pointsInROI=array([], shape=(0, 3), dtype=float64), **kwargs):
    """Find the points that are NOT in the input sets


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: input positions

		 nbSet: number of sets to complement

		 indices: indices of the point in the ROI

		 pointsInROI: points in the ROI


    """
    return attachedTo.createObject("ComplementaryROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, nbSet=nbSet, indices=indices, pointsInROI=pointsInROI, **kwargs)
