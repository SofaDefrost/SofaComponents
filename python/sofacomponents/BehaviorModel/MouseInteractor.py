# -*- coding: utf-8 -*-


"""
Component MouseInteractor

.. autofunction:: MouseInteractor

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MouseInteractor(attachedTo , name='MouseInteractor', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, **kwargs):
    """Perform tasks related to the interaction with the mouse
Perform tasks related to the interaction with the mouse and rigid objects


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("MouseInteractor" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, **kwargs)
