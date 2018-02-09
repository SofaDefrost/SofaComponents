# -*- coding: utf-8 -*-


"""
Component DirectSAP

.. autofunction:: DirectSAP

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DirectSAP(attachedTo , name='DirectSAP', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, draw=0, box=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], **kwargs):
    """Collision detection using sweep and prune


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 draw: enable/disable display of results

		 box: if not empty, objects that do not intersect this bounding-box will be ignored


    """
    return attachedTo.createObject("DirectSAP" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, draw=draw, box=box, **kwargs)
