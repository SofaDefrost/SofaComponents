# -*- coding: utf-8 -*-


"""
Component DataMonitor

.. autofunction:: DataMonitor

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DataMonitor(attachedTo , name='DataMonitor', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, data='', **kwargs):
    """DataMonitor


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 data: Monitored data


    """
    return attachedTo.createObject("DataMonitor" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, data=data, **kwargs)
