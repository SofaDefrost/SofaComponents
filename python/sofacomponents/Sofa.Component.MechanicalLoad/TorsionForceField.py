# -*- coding: utf-8 -*-


"""
Component TorsionForceField

.. autofunction:: TorsionForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TorsionForceField(attachedTo , name='TorsionForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, indices=array([], dtype=int32), torque=0.0, axis=array([0., 0., 0.]), origin=array([0., 0., 0.]), **kwargs):
    """Applies a torque to specified points


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 indices: indices of the selected points

		 torque: torque to apply

		 axis: direction of the axis (will be normalized)

		 origin: origin of the axis


    """
    return attachedTo.createObject("TorsionForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, indices=indices, torque=torque, axis=axis, origin=origin, **kwargs)
