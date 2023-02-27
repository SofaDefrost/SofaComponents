# -*- coding: utf-8 -*-


"""
Component PlaneForceField

.. autofunction:: PlaneForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PlaneForceField(attachedTo , name='PlaneForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, normal=array([0., 1., 0.]), d=0.0, stiffness=500.0, damping=5.0, maxForce=0.0, bilateral=0, localRange=array([-1, -1], dtype=int32), showPlane=0, planeColor=array([0. , 0.5, 0.2, 1. ], dtype=float32), showPlaneSize=10.0, **kwargs):
    """Repulsion applied by a plane toward the exterior (half-space)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 normal: plane normal. (default=[0,1,0])

		 d: plane d coef. (default=0)

		 stiffness: force stiffness. (default=500)

		 damping: force damping. (default=5)

		 maxForce: if non-null , the max force that can be applied to the object. (default=0)

		 bilateral: if true the plane force field is applied on both sides. (default=false)

		 localRange: optional range of local DOF indices. Any computation involving indices outside of this range are discarded (useful for parallelization using mesh partitionning)

		 showPlane: enable/disable drawing of plane. (default=false)

		 planeColor: plane color. (default=[0.0,0.5,0.2,1.0])

		 showPlaneSize: plane display size if draw is enabled. (default=10)


    """
    return attachedTo.createObject("PlaneForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, normal=normal, d=d, stiffness=stiffness, damping=damping, maxForce=maxForce, bilateral=bilateral, localRange=localRange, showPlane=showPlane, planeColor=planeColor, showPlaneSize=showPlaneSize, **kwargs)
