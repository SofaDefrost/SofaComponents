# -*- coding: utf-8 -*-


"""
Component HexahedronFEMForceField

.. autofunction:: HexahedronFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HexahedronFEMForceField(attachedTo , poissonRatio, youngModulus, name='HexahedronFEMForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, stiffnessMatrices=[], initialPoints=[], method='large', updateStiffnessMatrix=0, assembling=0, gatherPt=' ', gatherBsize=' ', drawing=1, drawPercentageOffset=0.15, **kwargs):
    """Hexahedral finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 stiffnessMatrices: Stiffness matrices per element (K_i)

		 initialPoints: Initial Position

		 method: "large" or "polar" or "small" displacements

		 poissonRatio: 

		 youngModulus: 

		 updateStiffnessMatrix: 

		 assembling: 

		 gatherPt: number of dof accumulated per threads during the gather operation (Only use in GPU version)

		 gatherBsize: number of dof accumulated per threads during the gather operation (Only use in GPU version)

		 drawing:  draw the forcefield if true

		 drawPercentageOffset: size of the hexa


    """
    return attachedTo.createObject("HexahedronFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, stiffnessMatrices=stiffnessMatrices, initialPoints=initialPoints, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, updateStiffnessMatrix=updateStiffnessMatrix, assembling=assembling, gatherPt=gatherPt, gatherBsize=gatherBsize, drawing=drawing, drawPercentageOffset=drawPercentageOffset, **kwargs)
