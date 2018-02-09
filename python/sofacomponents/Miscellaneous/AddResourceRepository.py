# -*- coding: utf-8 -*-


"""
Component AddResourceRepository

.. autofunction:: AddResourceRepository

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AddResourceRepository(attachedTo , name='AddResourceRepository', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, path='', **kwargs):
    """Add a repository to the pool of resources


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 path: Path to add to the pool of resources


    """
    return attachedTo.createObject("AddResourceRepository" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, path=path, **kwargs)
