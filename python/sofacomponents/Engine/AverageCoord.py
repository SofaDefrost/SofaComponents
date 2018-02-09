# -*- coding: utf-8 -*-


"""
Component AverageCoord

.. autofunction:: AverageCoord

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AverageCoord(attachedTo , name='AverageCoord', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, indices=[], vecId=1, average=[[0.0, 0.0, 0.0]], **kwargs):
    """Compute the average of coordinates


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 indices: indices of the coordinates to average

		 vecId: index of the vector (default value corresponds to core::VecCoordId::position() )

		 average: average of the values with the given indices in the given coordinate vector 
(default value corresponds to the average coord of the mechanical context)


    """
    return attachedTo.createObject("AverageCoord" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, indices=indices, vecId=vecId, average=average, **kwargs)
