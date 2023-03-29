# -*- coding: utf-8 -*-


"""
Component TriangleFEMForceField

.. autofunction:: TriangleFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangleFEMForceField(attachedTo , poissonRatio, youngModulus, name='TriangleFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, initialPoints=array([], shape=(0, 3), dtype=float64), method='large', thickness=1.0, planeStrain=0, **kwargs):
    """Triangular finite elements for static topology


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 initialPoints: Initial Position

		 method: large: large displacements, small: small displacements

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young modulus in Hooke's law

		 thickness: Thickness of the elements

		 planeStrain: Plane strain or plane stress assumption


    """
    return attachedTo.createObject("TriangleFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, initialPoints=initialPoints, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, thickness=thickness, planeStrain=planeStrain, **kwargs)
