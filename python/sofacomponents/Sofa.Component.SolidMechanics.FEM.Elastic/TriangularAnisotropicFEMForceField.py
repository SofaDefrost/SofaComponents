# -*- coding: utf-8 -*-


"""
Component TriangularAnisotropicFEMForceField

.. autofunction:: TriangularAnisotropicFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangularAnisotropicFEMForceField(attachedTo , poissonRatio, youngModulus, transverseYoungModulus, name='TriangularAnisotropicFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, triangleInfo=[], vertexInfo=[], method='large', rotatedInitialElements=array([], shape=(0, 9), dtype=float64), initialTransformation=array([], shape=(0, 9), dtype=float64), hosfordExponant=1.0, criteriaValue=1000000000000000.0, showStressValue=1, showStressVector=0, showFracturableTriangles=0, computePrincipalStress=0, fiberAngle=0.0, fiberCenter=array([], shape=(0, 3), dtype=float64), showFiber=1, localFiberDirection=array([], shape=(0, 3), dtype=float64), **kwargs):
    """Triangular finite element model using anisotropic material


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 triangleInfo: Internal triangle data

		 vertexInfo: Internal point data

		 method: large: large displacements, small: small displacements

		 poissonRatio: Poisson ratio in Hooke's law (vector)

		 youngModulus: Young modulus in Hooke's law (vector)

		 rotatedInitialElements: Flag activating rendering of stress directions within each triangle

		 initialTransformation: Flag activating rendering of stress directions within each triangle

		 hosfordExponant: Exponant in the Hosford yield criteria

		 criteriaValue: Fracturable threshold used to draw fracturable triangles

		 showStressValue: Flag activating rendering of stress values as a color in each triangle

		 showStressVector: Flag activating rendering of stress directions within each triangle

		 showFracturableTriangles: Flag activating rendering of triangles to fracture

		 computePrincipalStress: Compute principal stress for each triangle

		 transverseYoungModulus: transverseYoungModulus

		 fiberAngle: Fiber angle in global reference frame (in degrees)

		 fiberCenter: Concentric fiber center in global reference frame

		 showFiber: Flag activating rendering of fiber directions within each triangle

		 localFiberDirection: Computed fibers direction within each triangle


    """
    return attachedTo.createObject("TriangularAnisotropicFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, triangleInfo=triangleInfo, vertexInfo=vertexInfo, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, rotatedInitialElements=rotatedInitialElements, initialTransformation=initialTransformation, hosfordExponant=hosfordExponant, criteriaValue=criteriaValue, showStressValue=showStressValue, showStressVector=showStressVector, showFracturableTriangles=showFracturableTriangles, computePrincipalStress=computePrincipalStress, transverseYoungModulus=transverseYoungModulus, fiberAngle=fiberAngle, fiberCenter=fiberCenter, showFiber=showFiber, localFiberDirection=localFiberDirection, **kwargs)
