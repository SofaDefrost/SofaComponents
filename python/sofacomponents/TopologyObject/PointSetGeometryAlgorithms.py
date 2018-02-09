# -*- coding: utf-8 -*-


"""
Component PointSetGeometryAlgorithms

.. autofunction:: PointSetGeometryAlgorithms

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PointSetGeometryAlgorithms(attachedTo , name='PointSetGeometryAlgorithms', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, showIndicesScale=0.019999999552965164, showPointIndices=0, tagMechanics='', **kwargs):
    """Point set geometry algorithms


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 showIndicesScale: Debug : scale for view topology indices

		 showPointIndices: Debug : view Point indices

		 tagMechanics: Tag of the Mechanical Object


    """
    return attachedTo.createObject("PointSetGeometryAlgorithms" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, showIndicesScale=showIndicesScale, showPointIndices=showPointIndices, tagMechanics=tagMechanics, **kwargs)
