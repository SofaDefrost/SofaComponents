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

        
def HexahedronFEMForceField(attachedTo , poissonRatio, youngModulus, name='HexahedronFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, method='large', updateStiffnessMatrix=0, gatherPt=' ', gatherBsize=' ', drawing=1, drawPercentageOffset=0.15, stiffnessMatrices=array([], shape=(0, 576), dtype=float64), initialPoints=array([], shape=(0, 3), dtype=float64), **kwargs):
    """Hexahedral finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 method: "large" or "polar" or "small" displacements

		 poissonRatio: FEM Poisson Ratio in Hooke's law [0,0.5[

		 youngModulus: FEM Young's modulus in Hooke's law

		 updateStiffnessMatrix: 

		 gatherPt: number of dof accumulated per threads during the gather operation (Only use in GPU version)

		 gatherBsize: number of dof accumulated per threads during the gather operation (Only use in GPU version)

		 drawing: draw the forcefield if true

		 drawPercentageOffset: size of the hexa

		 stiffnessMatrices: Stiffness matrices per element (K_i)

		 initialPoints: Initial Position


    """
    return attachedTo.createObject("HexahedronFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, updateStiffnessMatrix=updateStiffnessMatrix, gatherPt=gatherPt, gatherBsize=gatherBsize, drawing=drawing, drawPercentageOffset=drawPercentageOffset, stiffnessMatrices=stiffnessMatrices, initialPoints=initialPoints, **kwargs)
