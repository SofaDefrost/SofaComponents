# -*- coding: utf-8 -*-


"""
Component ConicalForceField

.. autofunction:: ConicalForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ConicalForceField(attachedTo , name='ConicalForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, coneCenter=array([0., 0., 0.]), coneHeight=array([0., 0., 0.]), coneAngle=10.0, stiffness=500.0, damping=5.0, color=array([0., 0., 1., 1.], dtype=float32), **kwargs):
    """Repulsion applied by a cone toward the exterior


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 coneCenter: cone center

		 coneHeight: cone height

		 coneAngle: cone angle

		 stiffness: force stiffness

		 damping: force damping

		 color: cone color. (default=0.0,0.0,0.0,1.0,1.0)


    """
    return attachedTo.createObject("ConicalForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, coneCenter=coneCenter, coneHeight=coneHeight, coneAngle=coneAngle, stiffness=stiffness, damping=damping, color=color, **kwargs)
