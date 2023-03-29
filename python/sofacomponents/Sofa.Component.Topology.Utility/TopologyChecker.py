# -*- coding: utf-8 -*-


"""
Component TopologyChecker

.. autofunction:: TopologyChecker

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TopologyChecker(attachedTo , name='TopologyChecker', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, eachStep=0, **kwargs):
    """Read topological Changes and process them.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 eachStep: Check topology at each step


    """
    return attachedTo.createObject("TopologyChecker" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, eachStep=eachStep, **kwargs)
