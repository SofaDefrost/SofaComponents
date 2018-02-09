# -*- coding: utf-8 -*-


"""
Component HexahedralFEMForceFieldAndMass

.. autofunction:: HexahedralFEMForceFieldAndMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HexahedralFEMForceFieldAndMass(attachedTo , poissonRatio, youngModulus, name='HexahedralFEMForceFieldAndMass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, method='large', drawing=1, hexahedronInfo='', density=1.0, lumpedMass=0, massMatrices=[], totalMass=[], particleMasses=[], lumpedMasses=[], **kwargs):
    """Hexahedral finite elements with mass


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

		 method: "large" or "polar" displacements

		 poissonRatio: 

		 youngModulus: 

		 drawing:  draw the forcefield if true

		 hexahedronInfo: Internal hexahedron data

		 density: density == volumetric mass in english (kg.m-3)

		 lumpedMass: Does it use lumped masses?

		 massMatrices: Mass matrices per element (M_i)

		 totalMass: Total mass per element

		 particleMasses: Mass per particle

		 lumpedMasses: Lumped masses


    """
    return attachedTo.createObject("HexahedralFEMForceFieldAndMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, drawing=drawing, hexahedronInfo=hexahedronInfo, density=density, lumpedMass=lumpedMass, massMatrices=massMatrices, totalMass=totalMass, particleMasses=particleMasses, lumpedMasses=lumpedMasses, **kwargs)
