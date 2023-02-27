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

        
def BruteForceDetection(attachedTo , name='BruteForceDetection', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, **kwargs):
    """Combination of brute force broad phase and BVH narrow phase collision detection


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("BruteForceDetection" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, **kwargs)
