# -*- coding: utf-8 -*-


"""
Component DampVelocitySolver

.. autofunction:: DampVelocitySolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DampVelocitySolver(attachedTo , name='DampVelocitySolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, rate=0.99, threshold=0.0, **kwargs):
    """Reduce the velocities


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 rate: Factor used to reduce the velocities. Typically between 0 and 1.

		 threshold: Threshold under which the velocities are canceled.


    """
    return attachedTo.createObject("DampVelocitySolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, rate=rate, threshold=threshold, **kwargs)
