# -*- coding: utf-8 -*-


"""
Component BruteForceDetection

.. autofunction:: BruteForceDetection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BruteForceDetection(attachedTo , name='BruteForceDetection', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, box=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], **kwargs):
    """Collision detection using extensive pair-wise tests


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 box: if not empty, objects that do not intersect this bounding-box will be ignored


    """
    return attachedTo.createObject("BruteForceDetection" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, box=box, **kwargs)
