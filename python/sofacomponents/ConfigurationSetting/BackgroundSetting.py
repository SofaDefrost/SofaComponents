# -*- coding: utf-8 -*-


"""
Component BackgroundSetting

.. autofunction:: BackgroundSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BackgroundSetting(attachedTo , name='BackgroundSetting', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, color='1 1 1 1', image='', **kwargs):
    """Background colour setting


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 color: Color of the Background of the Viewer

		 image: Image to be used as background of the viewer


    """
    return attachedTo.createObject("BackgroundSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, color=color, image=image, **kwargs)
