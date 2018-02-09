# -*- coding: utf-8 -*-


"""
Component SphereForceField

.. autofunction:: SphereForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SphereForceField(attachedTo , name='SphereForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, contacts='', center=[[0.0, 0.0, 0.0]], radius=1.0, stiffness=500.0, damping=5.0, color='0 0 1 1', draw=1, localRange=[[-1, -1]], bilateral=0, **kwargs):
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

		 localRange: optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)

		 bilateral: if true the sphere force field is applied on both sides


    """
    return attachedTo.createObject("SphereForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, contacts=contacts, center=center, radius=radius, stiffness=stiffness, damping=damping, color=color, draw=draw, localRange=localRange, bilateral=bilateral, **kwargs)
