# -*- coding: utf-8 -*-


"""
Component AddDataRepository

.. autofunction:: AddDataRepository

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AddDataRepository(attachedTo , name='AddDataRepository', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Valid', listening=0, path='C:/Users/Alex/Dev/SofaComponents/python/', **kwargs):
    """Add a path to DataRepository


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 path: Path to add to the pool of resources


    """
    return attachedTo.createObject("AddDataRepository" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, path=path, **kwargs)
