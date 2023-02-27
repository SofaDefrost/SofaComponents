# -*- coding: utf-8 -*-


"""
Component UniformVelocityDampingForceField

.. autofunction:: UniformVelocityDampingForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def UniformVelocityDampingForceField(attachedTo , name='UniformVelocityDampingForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, dampingCoefficient=0.1, implicit=0, **kwargs):
    """Uniform velocity damping


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 dampingCoefficient: velocity damping coefficient

		 implicit: should it generate damping matrix df/dv? (explicit otherwise, i.e. only generating a force)


    """
    return attachedTo.createObject("UniformVelocityDampingForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, dampingCoefficient=dampingCoefficient, implicit=implicit, **kwargs)
