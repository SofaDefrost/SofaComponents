# -*- coding: utf-8 -*-


"""
Component MergeROIs

.. autofunction:: MergeROIs

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MergeROIs(attachedTo , name='MergeROIs', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, nbROIs=0, roiIndices='', **kwargs):
    """Merge a list of ROIs (vector<Indices>) into a single Data (vector<svector<Indices>>)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 nbROIs: size of indices/value vector

		 roiIndices: Vector of ROIs


    """
    return attachedTo.createObject("MergeROIs" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, nbROIs=nbROIs, roiIndices=roiIndices, **kwargs)
