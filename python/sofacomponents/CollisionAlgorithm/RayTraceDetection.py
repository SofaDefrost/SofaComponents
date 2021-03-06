# -*- coding: utf-8 -*-


"""
Component RayTraceDetection

.. autofunction:: RayTraceDetection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RayTraceDetection(attachedTo , name='RayTraceDetection', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, draw=0, **kwargs):
    """Collision detection using TriangleOctreeModel


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 draw: enable/disable display of results


    """
    return attachedTo.createObject("RayTraceDetection" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, draw=draw, **kwargs)
