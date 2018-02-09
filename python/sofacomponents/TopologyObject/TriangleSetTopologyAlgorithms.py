# -*- coding: utf-8 -*-


"""
Component TriangleSetTopologyAlgorithms

.. autofunction:: TriangleSetTopologyAlgorithms

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangleSetTopologyAlgorithms(attachedTo , name='TriangleSetTopologyAlgorithms', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, RemoveTrianglesByIndex=[], addTrianglesByIndex=[], **kwargs):
    """Triangle set topology algorithms


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 RemoveTrianglesByIndex: Debug : Remove a triangle or a list of triangles by using their indices (only while animate).

		 addTrianglesByIndex: Debug : Add a triangle or a list of triangles by using their indices (only while animate).


    """
    return attachedTo.createObject("TriangleSetTopologyAlgorithms" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, RemoveTrianglesByIndex=RemoveTrianglesByIndex, addTrianglesByIndex=addTrianglesByIndex, **kwargs)
