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

        
def RayTraceDetection(attachedTo , name='RayTraceDetection', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, **kwargs):
    """Collision detection using TriangleOctreeModel


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("RayTraceDetection" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, **kwargs)
