# -*- coding: utf-8 -*-


"""
Component WarpPreconditioner

.. autofunction:: WarpPreconditioner

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def WarpPreconditioner(attachedTo , name='WarpPreconditioner', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, useRotationFinder=0, update_step=1, **kwargs):
    """Linear system solver wrapping another (precomputed) linear solver by a per-node rotation matrix


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 useRotationFinder: Which rotation Finder to use

		 update_step: Number of steps before the next refresh of the system matrix in the main solver


    """
    return attachedTo.createObject("WarpPreconditioner" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, useRotationFinder=useRotationFinder, update_step=update_step, **kwargs)
