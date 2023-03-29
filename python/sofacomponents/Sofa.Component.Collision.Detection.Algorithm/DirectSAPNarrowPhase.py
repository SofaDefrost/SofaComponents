# -*- coding: utf-8 -*-


"""
Component DirectSAPNarrowPhase

.. autofunction:: DirectSAPNarrowPhase

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DirectSAPNarrowPhase(attachedTo , name='DirectSAPNarrowPhase', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, draw=0, showOnlyInvestigatedBoxes=1, nbPairs=0, **kwargs):
    """Collision detection using sweep and prune


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 draw: enable/disable display of results

		 showOnlyInvestigatedBoxes: Show only boxes which will be sent to narrow phase

		 nbPairs: number of pairs of elements sent to narrow phase


    """
    return attachedTo.createObject("DirectSAPNarrowPhase" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, draw=draw, showOnlyInvestigatedBoxes=showOnlyInvestigatedBoxes, nbPairs=nbPairs, **kwargs)
