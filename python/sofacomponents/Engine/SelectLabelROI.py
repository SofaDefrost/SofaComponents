# -*- coding: utf-8 -*-


"""
Component SelectLabelROI

.. autofunction:: SelectLabelROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SelectLabelROI(attachedTo , name='SelectLabelROI', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, labels='', selectLabels=[], indices=[], **kwargs):
    """Select a subset of labeled points or cells stored in (vector<svector<label>>) given certain labels


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 labels: lists of labels associated to each point/cell

		 selectLabels: list of selected labels

		 indices: selected point/cell indices


    """
    return attachedTo.createObject("SelectLabelROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, labels=labels, selectLabels=selectLabels, indices=indices, **kwargs)
