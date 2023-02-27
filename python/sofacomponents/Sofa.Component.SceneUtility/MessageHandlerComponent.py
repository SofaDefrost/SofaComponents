# -*- coding: utf-8 -*-


"""
Component MessageHandlerComponent

.. autofunction:: MessageHandlerComponent

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MessageHandlerComponent(attachedTo , name='MessageHandlerComponent', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, handler='', **kwargs):
    """This object controls the way Sofa print's info/warning/error/fatal messages. 


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 handler: Type of the message handler to use among [sofa, clang                                        //, log                                        , silent]. 


    """
    return attachedTo.createObject("MessageHandlerComponent" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, handler=handler, **kwargs)
