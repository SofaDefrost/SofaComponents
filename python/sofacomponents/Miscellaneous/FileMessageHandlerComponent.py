# -*- coding: utf-8 -*-


"""
Component FileMessageHandlerComponent

.. autofunction:: FileMessageHandlerComponent

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FileMessageHandlerComponent(attachedTo , name='FileMessageHandlerComponent', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, filename='', **kwargs):
    """This component dump all the messages intoa file.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 filename: Name of the file into which the message will be saved in.


    """
    return attachedTo.createObject("FileMessageHandlerComponent" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, **kwargs)
