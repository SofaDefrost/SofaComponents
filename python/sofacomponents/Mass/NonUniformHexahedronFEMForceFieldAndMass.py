# -*- coding: utf-8 -*-


"""
Component NonUniformHexahedronFEMForceFieldAndMass

.. autofunction:: NonUniformHexahedronFEMForceFieldAndMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NonUniformHexahedronFEMForceFieldAndMass(attachedTo , poissonRatio, youngModulus, name='NonUniformHexahedronFEMForceFieldAndMass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, stiffnessMatrices=[], initialPoints=[], method='large', updateStiffnessMatrix=0, assembling=0, gatherPt=' ', gatherBsize=' ', drawing=1, drawPercentageOffset=0.15, massMatrices=[], density=1.0, lumpedMass=0, nbVirtualFinerLevels=0, useMass=1, totalMass=0.0, **kwargs):
    """Non uniform Hexahedral finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 separateGravity: add separately gravity to velocity computation

		 rayleighMass: Rayleigh damping - mass matrix coefficient

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

		 massMatrices: Mass matrices per element (M_i)

		 density: density == volumetric mass in english (kg.m-3)

		 lumpedMass: Does it use lumped masses?

		 nbVirtualFinerLevels: use virtual finer levels, in order to compte non-uniform stiffness

		 useMass: Using this ForceField like a Mass? (rather than using a separated Mass)

		 totalMass: 


    """
    return attachedTo.createObject("NonUniformHexahedronFEMForceFieldAndMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, stiffnessMatrices=stiffnessMatrices, initialPoints=initialPoints, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, updateStiffnessMatrix=updateStiffnessMatrix, assembling=assembling, gatherPt=gatherPt, gatherBsize=gatherBsize, drawing=drawing, drawPercentageOffset=drawPercentageOffset, massMatrices=massMatrices, density=density, lumpedMass=lumpedMass, nbVirtualFinerLevels=nbVirtualFinerLevels, useMass=useMass, totalMass=totalMass, **kwargs)
