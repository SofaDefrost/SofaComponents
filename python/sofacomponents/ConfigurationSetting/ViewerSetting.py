# -*- coding: utf-8 -*-


"""
Component ViewerSetting

.. autofunction:: ViewerSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ViewerSetting(attachedTo , name='ViewerSetting', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, resolution=[[800, 600]], fullscreen=0, cameraMode='Perspective', objectPickingMethod='Ray casting', **kwargs):
    """Configuration for the Viewer of your application


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 resolution: resolution of the Viewer

		 fullscreen: Fullscreen mode

		 cameraMode: Camera mode

		 objectPickingMethod: The method used to pick objects


    """
    return attachedTo.createObject("ViewerSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, resolution=resolution, fullscreen=fullscreen, cameraMode=cameraMode, objectPickingMethod=objectPickingMethod, **kwargs)
