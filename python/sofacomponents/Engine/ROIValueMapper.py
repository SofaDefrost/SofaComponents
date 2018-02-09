# -*- coding: utf-8 -*-


"""
Component ROIValueMapper

.. autofunction:: ROIValueMapper

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ROIValueMapper(attachedTo , name='ROIValueMapper', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, nbROIs=0, outputValues=[], defaultValue=0.0, **kwargs):
    """Generate a list of values from value-indices pairs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 nbROIs: size of indices/value vector

		 outputValues: New vector of values

		 defaultValue: Default value for indices out of ROIs


    """
    return attachedTo.createObject("ROIValueMapper" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, nbROIs=nbROIs, outputValues=outputValues, defaultValue=defaultValue, **kwargs)
