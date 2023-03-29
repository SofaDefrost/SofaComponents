# -*- coding: utf-8 -*-


"""
Component TetrahedralCorotationalFEMForceField

.. autofunction:: TetrahedralCorotationalFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedralCorotationalFEMForceField(attachedTo , poissonRatio, youngModulus, name='TetrahedralCorotationalFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, tetrahedronInfo=[], method='large', localStiffnessFactor=array([], dtype=float64), updateStiffnessMatrix=0, computeGlobalMatrix=0, drawing=1, drawColor1=array([0., 0., 1., 1.], dtype=float32), drawColor2=array([0. , 0.5, 1. , 1. ], dtype=float32), drawColor3=array([0., 1., 1., 1.], dtype=float32), drawColor4=array([0.5, 1. , 1. , 1. ], dtype=float32), **kwargs):
    """Corotational FEM Tetrahedral finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 tetrahedronInfo: Internal tetrahedron data

		 method: "small", "large" (by QR) or "polar" displacements

		 poissonRatio: FEM Poisson Ratio

		 youngModulus: FEM Young Modulus

		 localStiffnessFactor: Allow specification of different stiffness per element. If there are N element and M values are specified, the youngModulus factor for element i would be localStiffnessFactor[i*M/N]

		 updateStiffnessMatrix: 

		 computeGlobalMatrix: 

		 drawing:  draw the forcefield if true

		 drawColor1:  draw color for faces 1

		 drawColor2:  draw color for faces 2

		 drawColor3:  draw color for faces 3

		 drawColor4:  draw color for faces 4


    """
    return attachedTo.createObject("TetrahedralCorotationalFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, tetrahedronInfo=tetrahedronInfo, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, localStiffnessFactor=localStiffnessFactor, updateStiffnessMatrix=updateStiffnessMatrix, computeGlobalMatrix=computeGlobalMatrix, drawing=drawing, drawColor1=drawColor1, drawColor2=drawColor2, drawColor3=drawColor3, drawColor4=drawColor4, **kwargs)
