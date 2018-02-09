# -*- coding: utf-8 -*-


"""
Component StartNavigationButtonSetting

.. autofunction:: StartNavigationButtonSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def StartNavigationButtonSetting(attachedTo , name='StartNavigationButtonSetting', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, button='Left', **kwargs):
    """Start Navigation Button configuration


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 button: Mouse button used


    """
    return attachedTo.createObject("StartNavigationButtonSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, button=button, **kwargs)
