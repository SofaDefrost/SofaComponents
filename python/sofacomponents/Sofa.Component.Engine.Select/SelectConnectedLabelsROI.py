# -*- coding: utf-8 -*-


"""
Component SelectConnectedLabelsROI

.. autofunction:: SelectConnectedLabelsROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SelectConnectedLabelsROI(attachedTo , name='SelectConnectedLabelsROI', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, nbLabels=0, connectLabels=array([], dtype=int32), indices=array([], dtype=int32), **kwargs):
    """Select a subset of points or cells labeled from different sources, that are connected given a list of connection pairs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 nbLabels: number of label lists

		 connectLabels: Pairs of label to be connected accross different label lists

		 indices: selected point/cell indices


    """
    return attachedTo.createObject("SelectConnectedLabelsROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, nbLabels=nbLabels, connectLabels=connectLabels, indices=indices, **kwargs)
