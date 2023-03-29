# -*- coding: utf-8 -*-


"""
Component BruteForceBroadPhase

.. autofunction:: BruteForceBroadPhase

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BruteForceBroadPhase(attachedTo , name='BruteForceBroadPhase', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, box=array([[0., 0., 0.],
       [0., 0., 0.]]), **kwargs):
    """Broad phase collision detection using extensive pair-wise tests


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 box: if not empty, objects that do not intersect this bounding-box will be ignored


    """
    return attachedTo.createObject("BruteForceBroadPhase" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, box=box, **kwargs)
