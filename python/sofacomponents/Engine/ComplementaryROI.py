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

        
def ComplementaryROI(attachedTo , name='ComplementaryROI', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[], nbSet=0, indices=[], pointsInROI=[], **kwargs):
    """Find the points that are NOT in the input sets


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: input positions

		 nbSet: number of sets to complement

		 indices: indices of the point in the ROI

		 pointsInROI: points in the ROI


    """
    return attachedTo.createObject("ComplementaryROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, nbSet=nbSet, indices=indices, pointsInROI=pointsInROI, **kwargs)
