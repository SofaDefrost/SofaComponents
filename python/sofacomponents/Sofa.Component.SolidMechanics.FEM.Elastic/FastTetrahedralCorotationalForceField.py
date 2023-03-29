# -*- coding: utf-8 -*-


"""
Component FastTetrahedralCorotationalForceField

.. autofunction:: FastTetrahedralCorotationalForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FastTetrahedralCorotationalForceField(attachedTo , poissonRatio, youngModulus, name='FastTetrahedralCorotationalForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, pointInfo=array([], shape=(0, 9), dtype=float64), edgeInfo=array([], shape=(0, 9), dtype=float64), tetrahedronInfo=[], method='qr', drawing=1, drawColor1=array([0., 0., 1., 1.], dtype=float32), drawColor2=array([0. , 0.5, 1. , 1. ], dtype=float32), drawColor3=array([0., 1., 1., 1.], dtype=float32), drawColor4=array([0.5, 1. , 1. , 1. ], dtype=float32), **kwargs):
    """Fast Corotational Tetrahedral Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 pointInfo: Internal point data

		 edgeInfo: Internal edge data

		 tetrahedronInfo: Internal tetrahedron data

		 method:  method for rotation computation :"qr" (by QR) or "polar" or "polar2" or "none" (Linear elastic) 

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young modulus in Hooke's law

		 drawing:  draw the forcefield if true

		 drawColor1:  draw color for faces 1

		 drawColor2:  draw color for faces 2

		 drawColor3:  draw color for faces 3

		 drawColor4:  draw color for faces 4


    """
    return attachedTo.createObject("FastTetrahedralCorotationalForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, pointInfo=pointInfo, edgeInfo=edgeInfo, tetrahedronInfo=tetrahedronInfo, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, drawing=drawing, drawColor1=drawColor1, drawColor2=drawColor2, drawColor3=drawColor3, drawColor4=drawColor4, **kwargs)
