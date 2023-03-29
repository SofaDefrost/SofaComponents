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

        
def SphereForceField(attachedTo , name='SphereForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, contacts=[], center=array([0., 0., 0.]), radius=1.0, stiffness=500.0, damping=5.0, color=array([0., 0., 1., 1.], dtype=float32), localRange=array([-1, -1], dtype=int32), bilateral=0, **kwargs):
    """Repulsion applied by a sphere toward the exterior


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

		 center: sphere center

		 radius: sphere radius

		 stiffness: force stiffness

		 damping: force damping

		 color: sphere color. (default=[0,0,1,1])

		 localRange: optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)

		 bilateral: if true the sphere force field is applied on both sides


    """
    return attachedTo.createObject("SphereForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, contacts=contacts, center=center, radius=radius, stiffness=stiffness, damping=damping, color=color, localRange=localRange, bilateral=bilateral, **kwargs)
