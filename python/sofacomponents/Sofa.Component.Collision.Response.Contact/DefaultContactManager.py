# -*- coding: utf-8 -*-


"""
Component DefaultContactManager

.. autofunction:: DefaultContactManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DefaultContactManager(attachedTo , name='DefaultContactManager', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, response='PenalityContactForceField', responseParams='', **kwargs):
    """Default class to create reactions to the collisions


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 response: contact response class

		 responseParams: contact response parameters (syntax: name1=value1&name2=value2&...)


    """
    return attachedTo.createObject("DefaultContactManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, response=response, responseParams=responseParams, **kwargs)
