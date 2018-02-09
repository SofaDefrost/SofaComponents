# -*- coding: utf-8 -*-


"""
Component SleepController

.. autofunction:: SleepController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SleepController(attachedTo , name='SleepController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, minTimeSinceWakeUp=0.1, immobileThreshold=0.001, rotationThreshold=0.0, **kwargs):
    """A controller that puts node into sleep when the objects are not moving, and wake them up again when there are in collision with a moving object


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 minTimeSinceWakeUp: Do not do anything before objects have been moving for this duration

		 immobileThreshold: Speed value under which we consider a particule to be immobile

		 rotationThreshold: If non null, this is the rotation speed value under which we consider a particule to be immobile


    """
    return attachedTo.createObject("SleepController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, minTimeSinceWakeUp=minTimeSinceWakeUp, immobileThreshold=immobileThreshold, rotationThreshold=rotationThreshold, **kwargs)
