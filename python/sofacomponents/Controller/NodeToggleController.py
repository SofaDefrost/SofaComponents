# -*- coding: utf-8 -*-


"""
Component NodeToggleController

.. autofunction:: NodeToggleController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NodeToggleController(attachedTo , name='NodeToggleController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, handleEventTriggersUpdate=0, key=42, nameNode='', initStatus=1, firstFrame=1, **kwargs):
    """Provides a way to switch active one of the children nodes.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 handleEventTriggersUpdate: Event handling frequency controls the controller update frequency

		 key: Key chosen for toggling the node(s)

		 nameNode: Name of a specific node to toggle

		 initStatus: If one node is chosen, this gives the initial status of the node

		 firstFrame: Toggle the node at first step


    """
    return attachedTo.createObject("NodeToggleController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, key=key, nameNode=nameNode, initStatus=initStatus, firstFrame=firstFrame, **kwargs)
