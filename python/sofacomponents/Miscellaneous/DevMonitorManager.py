# -*- coding: utf-8 -*-


"""
Component DevMonitorManager

.. autofunction:: DevMonitorManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DevMonitorManager(attachedTo , name='DevMonitorManager', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, period=1.0, indices=[], **kwargs):
    """DevMonitorManager


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 period: period between outputs

		 indices: Indices of the points which will be monitored


    """
    return attachedTo.createObject("DevMonitorManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, period=period, indices=indices, **kwargs)
