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

        
def FastTetrahedralCorotationalForceField(attachedTo , name='FastTetrahedralCorotationalForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, pointInfo=[], edgeInfo=[], tetrahedronInfo='', method='qr', poissonRatio=0.3, youngModulus=1000.0, drawing=1, drawColor1=[[0.0, 0.0, 1.0, 1.0]], drawColor2=[[0.0, 0.5, 1.0, 1.0]], drawColor3=[[0.0, 1.0, 1.0, 1.0]], drawColor4=[[0.5, 1.0, 1.0, 1.0]], **kwargs):
    """Fast Corotational Tetrahedral Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

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
    return attachedTo.createObject("FastTetrahedralCorotationalForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, pointInfo=pointInfo, edgeInfo=edgeInfo, tetrahedronInfo=tetrahedronInfo, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, drawing=drawing, drawColor1=drawColor1, drawColor2=drawColor2, drawColor3=drawColor3, drawColor4=drawColor4, **kwargs)
