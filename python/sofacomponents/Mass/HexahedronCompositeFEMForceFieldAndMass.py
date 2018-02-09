# -*- coding: utf-8 -*-


"""
Component HexahedronCompositeFEMForceFieldAndMass

.. autofunction:: HexahedronCompositeFEMForceFieldAndMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HexahedronCompositeFEMForceFieldAndMass(attachedTo , poissonRatio, youngModulus, name='HexahedronCompositeFEMForceFieldAndMass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, stiffnessMatrices=[], initialPoints=[], method='large', updateStiffnessMatrix=0, assembling=0, gatherPt=' ', gatherBsize=' ', drawing=1, drawPercentageOffset=0.15, massMatrices=[], density=1.0, lumpedMass=0, nbVirtualFinerLevels=0, useMass=1, totalMass=0.0, finestToCoarse=0, homogenizationMethod=0, completeInterpolation=0, useRamification=1, drawType=0, drawColor=0, drawSize=-1.0, **kwargs):
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

		 finestToCoarse: Does the homogenization is done directly from the finest level to the coarse one?

		 homogenizationMethod: 0->static, 1->constrained static, 2->modal analysis

		 completeInterpolation: Is the non-linear, complete interpolation used?

		 useRamification: If SparseGridRamification, are ramifications taken into account?

		 drawType: 

		 drawColor: 

		 drawSize: 


    """
    return attachedTo.createObject("HexahedronCompositeFEMForceFieldAndMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, stiffnessMatrices=stiffnessMatrices, initialPoints=initialPoints, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, updateStiffnessMatrix=updateStiffnessMatrix, assembling=assembling, gatherPt=gatherPt, gatherBsize=gatherBsize, drawing=drawing, drawPercentageOffset=drawPercentageOffset, massMatrices=massMatrices, density=density, lumpedMass=lumpedMass, nbVirtualFinerLevels=nbVirtualFinerLevels, useMass=useMass, totalMass=totalMass, finestToCoarse=finestToCoarse, homogenizationMethod=homogenizationMethod, completeInterpolation=completeInterpolation, useRamification=useRamification, drawType=drawType, drawColor=drawColor, drawSize=drawSize, **kwargs)
