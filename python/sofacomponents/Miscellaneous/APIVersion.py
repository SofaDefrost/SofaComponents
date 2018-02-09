# -*- coding: utf-8 -*-


"""
Component APIVersion

.. autofunction:: APIVersion

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def APIVersion(attachedTo , name='APIVersion', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, level='17.06', **kwargs):
    """Specify the APIVersion of the component used in a scene.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 level: The API Level of the scene ('17.06', '17.12', '18.06', ...)


    """
    return attachedTo.createObject("APIVersion" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, level=level, **kwargs)
