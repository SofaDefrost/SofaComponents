# -*- coding: utf-8 -*-


"""
Component DataController

.. autofunction:: DataController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DataController(attachedTo , name='DataController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, data='', **kwargs):
    """DataController


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 data: Controlled data


    """
    return attachedTo.createObject("DataController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, data=data, **kwargs)
