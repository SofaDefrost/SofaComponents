# -*- coding: utf-8 -*-


"""
Component FreeMotionAnimationLoop

.. autofunction:: FreeMotionAnimationLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FreeMotionAnimationLoop(attachedTo , name='FreeMotionAnimationLoop', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, solveVelocityConstraintFirst=0, **kwargs):
    """Constraint solver


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 solveVelocityConstraintFirst: solve separately velocity constraint violations before position constraint violations


    """
    return attachedTo.createObject("FreeMotionAnimationLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, solveVelocityConstraintFirst=solveVelocityConstraintFirst, **kwargs)
