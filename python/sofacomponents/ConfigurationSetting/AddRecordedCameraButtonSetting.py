# -*- coding: utf-8 -*-


"""
Component AddRecordedCameraButtonSetting

.. autofunction:: AddRecordedCameraButtonSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AddRecordedCameraButtonSetting(attachedTo , name='AddRecordedCameraButtonSetting', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, button='Left', **kwargs):
    """Save Camera's View Point Button configuration


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 button: Mouse button used


    """
    return attachedTo.createObject("AddRecordedCameraButtonSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, button=button, **kwargs)
