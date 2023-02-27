# -*- coding: utf-8 -*-


"""
Component CollisionPipeline

.. autofunction:: CollisionPipeline

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CollisionPipeline(attachedTo , name='CollisionPipeline', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, verbose=0, draw=0, depth=6, **kwargs):
    """The default collision detection and modeling pipeline


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 verbose: Display extra informations at each computation step. (default=false)

		 draw: Draw the detected collisions. (default=false)

		 depth: Max depth of bounding trees. (default=6, min=?, max=?)


    """
    return attachedTo.createObject("CollisionPipeline" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, verbose=verbose, draw=draw, depth=depth, **kwargs)
