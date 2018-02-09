# -*- coding: utf-8 -*-


"""
Component WashingMachineForceField

.. autofunction:: WashingMachineForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def WashingMachineForceField(attachedTo , name='WashingMachineForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, center=[[0.0, 0.0, 0.0]], size=[[1.0, 1.0, 1.0]], speed=0.001, axis=[[1.0, 0.0, 0.0]], stiffness=500.0, damping=5.0, **kwargs):
    """A custom force field


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 center: box center

		 size: box size

		 speed: rotation speed

		 axis: rotation axis

		 stiffness: penality force stiffness

		 damping: penality force damping


    """
    return attachedTo.createObject("WashingMachineForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, center=center, size=size, speed=speed, axis=axis, stiffness=stiffness, damping=damping, **kwargs)
