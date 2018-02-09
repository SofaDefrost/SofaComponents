# -*- coding: utf-8 -*-


"""
Component DiagonalVelocityDampingForceField

.. autofunction:: DiagonalVelocityDampingForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DiagonalVelocityDampingForceField(attachedTo , name='DiagonalVelocityDampingForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, dampingCoefficient=[], **kwargs):
    """Diagonal velocity damping


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 dampingCoefficient: velocity damping coefficients (by cinematic dof)


    """
    return attachedTo.createObject("DiagonalVelocityDampingForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, dampingCoefficient=dampingCoefficient, **kwargs)
