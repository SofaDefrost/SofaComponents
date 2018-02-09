# -*- coding: utf-8 -*-


"""
Component VaccumSphereForceField

.. autofunction:: VaccumSphereForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VaccumSphereForceField(attachedTo , name='VaccumSphereForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, contacts='', center=[[0.0, 0.0, 0.0]], radius=1.0, stiffness=500.0, damping=5.0, color='0 0 1 1', draw=1, centerState='', active=0, key=49, filter=0.0, **kwargs):
    """Repulsion applied by a sphere toward the exterior


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 contacts: Contacts

		 center: sphere center

		 radius: sphere radius

		 stiffness: force stiffness

		 damping: force damping

		 color: sphere color. (default=[0,0,1,1])

		 draw: enable/disable drawing of the sphere

		 centerState: path to the MechanicalState controlling the center point

		 active: Activate this object.
Note that this can be dynamically controlled by using a key

		 key: key to press to activate this object until the key is released

		 filter: filter


    """
    return attachedTo.createObject("VaccumSphereForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, contacts=contacts, center=center, radius=radius, stiffness=stiffness, damping=damping, color=color, draw=draw, centerState=centerState, active=active, key=key, filter=filter, **kwargs)
