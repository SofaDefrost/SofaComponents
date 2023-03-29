# -*- coding: utf-8 -*-


"""
Component MultiTagAnimationLoop

.. autofunction:: MultiTagAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MultiTagAnimationLoop(attachedTo , name='MultiTagAnimationLoop', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, computeBoundingBox=1, **kwargs):
    """Simple animation loop that given a list of tags, animate the graph one tag after another.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 computeBoundingBox: If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.


    """
    return attachedTo.createObject("MultiTagAnimationLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, computeBoundingBox=computeBoundingBox, **kwargs)
