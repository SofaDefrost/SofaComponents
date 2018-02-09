# -*- coding: utf-8 -*-


"""
Component EllipsoidForceField

.. autofunction:: EllipsoidForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EllipsoidForceField(attachedTo , name='EllipsoidForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, contacts='', center=[[0.0, 0.0, 0.0]], vradius=[[0.0, 0.0, 0.0]], stiffness=500.0, damping=5.0, color='0 0.5 1 1', draw=1, **kwargs):
    """Repulsion applied by an ellipsoid toward the exterior or the interior


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 contacts: Contacts

		 center: ellipsoid center

		 vradius: ellipsoid radius

		 stiffness: force stiffness (positive to repulse outward, negative inward)

		 damping: force damping

		 color: ellipsoid color. (default=0,0.5,1.0,1.0)

		 draw: enable/disable drawing of the ellipsoid


    """
    return attachedTo.createObject("EllipsoidForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, contacts=contacts, center=center, vradius=vradius, stiffness=stiffness, damping=damping, color=color, draw=draw, **kwargs)
