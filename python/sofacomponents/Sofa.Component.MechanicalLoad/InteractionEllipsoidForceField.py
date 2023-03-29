# -*- coding: utf-8 -*-


"""
Component InteractionEllipsoidForceField

.. autofunction:: InteractionEllipsoidForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def InteractionEllipsoidForceField(attachedTo , name='InteractionEllipsoidForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, contacts=[], center=array([], shape=(0, 3), dtype=float64), vradius=array([], shape=(0, 3), dtype=float64), stiffness=500.0, damping=5.0, color=array([0. , 0.5, 1. , 1. ], dtype=float32), draw=1, object2_dof_index=0, object2_forces=1, object2_invert=0, **kwargs):
    """Repulsion applied by an ellipsoid toward the exterior or the interior


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 contacts: Contacts

		 center: ellipsoid center

		 vradius: ellipsoid radius

		 stiffness: force stiffness (positive to repulse outward, negative inward)

		 damping: force damping

		 color: ellipsoid color. (default=[0.0,0.5,1.0,1.0])

		 draw: enable/disable drawing of the ellipsoid

		 object2_dof_index: Dof index of object 2 where the forcefield is attached

		 object2_forces: enable/disable propagation of forces to object 2

		 object2_invert: inverse transform from object 2 (use when object 1 is in local coordinates within a frame defined by object 2)


    """
    return attachedTo.createObject("InteractionEllipsoidForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, contacts=contacts, center=center, vradius=vradius, stiffness=stiffness, damping=damping, color=color, draw=draw, object2_dof_index=object2_dof_index, object2_forces=object2_forces, object2_invert=object2_invert, **kwargs)
