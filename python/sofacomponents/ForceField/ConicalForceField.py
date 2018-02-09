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

        
def ConicalForceField(attachedTo , name='ConicalForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, coneCenter=[[0.0, 0.0, 0.0]], coneHeight=[[0.0, 0.0, 0.0]], coneAngle=10.0, stiffness=500.0, damping=5.0, color='0 0 1 1', draw=1, **kwargs):
    """Repulsion applied by a cone toward the exterior


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 coneCenter: cone center

		 coneHeight: cone height

		 coneAngle: cone angle

		 stiffness: force stiffness

		 damping: force damping

		 color: cone color. (default=0.0,0.0,0.0,1.0,1.0)

		 draw: enable/disable drawing of the cone


    """
    return attachedTo.createObject("ConicalForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, coneCenter=coneCenter, coneHeight=coneHeight, coneAngle=coneAngle, stiffness=stiffness, damping=damping, color=color, draw=draw, **kwargs)
