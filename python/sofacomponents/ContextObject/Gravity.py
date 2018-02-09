# -*- coding: utf-8 -*-


"""
Component Gravity

.. autofunction:: Gravity

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Gravity(attachedTo , name='Gravity', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, gravity=[[0.0, 0.0, 0.0]], **kwargs):
    """Gravity in world coordinates


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 gravity: Gravity in the world coordinate system


    """
    return attachedTo.createObject("Gravity" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, gravity=gravity, **kwargs)
