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

        
def MultiTagAnimationLoop(attachedTo , name='MultiTagAnimationLoop', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, **kwargs):
    """Simple animation loop that given a list of tags, animate the graph one tag after another.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("MultiTagAnimationLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, **kwargs)
