# -*- coding: utf-8 -*-


"""
Component AngularSpringForceField

.. autofunction:: AngularSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AngularSpringForceField(attachedTo , name='AngularSpringForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, indices=array([], dtype=int32), angularStiffness=array([], dtype=float64), limit=array([], dtype=float64), drawSpring=0, springColor=array([0., 1., 0., 1.], dtype=float32), **kwargs):
    """Angular springs applied to rotational degrees of freedom of a rigid body or frame


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 indices: index of nodes controlled by the angular springs

		 angularStiffness: angular stiffness for the controlled nodes

		 limit: angular limit (max; min) values where the force applies

		 drawSpring: draw Spring

		 springColor: spring color


    """
    return attachedTo.createObject("AngularSpringForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, indices=indices, angularStiffness=angularStiffness, limit=limit, drawSpring=drawSpring, springColor=springColor, **kwargs)
