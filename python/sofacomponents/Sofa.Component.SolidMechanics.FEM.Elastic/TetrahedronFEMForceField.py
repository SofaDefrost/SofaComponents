# -*- coding: utf-8 -*-


"""
Component TetrahedronFEMForceField

.. autofunction:: TetrahedronFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedronFEMForceField(attachedTo , poissonRatio, youngModulus, name='TetrahedronFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, initialPoints=array([], shape=(0, 3), dtype=float64), method='large', localStiffnessFactor=array([], dtype=float64), updateStiffnessMatrix=0, computeGlobalMatrix=0, plasticMaxThreshold=0.0, plasticYieldThreshold=9.999999747378752e-05, plasticCreep=0.8999999761581421, gatherPt=' ', gatherBsize=' ', drawHeterogeneousTetra=0, computeVonMisesStress=0, vonMisesPerElement=array([], dtype=float64), vonMisesPerNode=array([], dtype=float64), vonMisesStressColors=array([], shape=(0, 4), dtype=float32), showStressColorMap='Blue to Red', showStressAlpha=1.0, showVonMisesStressPerNode=0, showVonMisesStressPerElement=0, updateStiffness=0, **kwargs):
    """Tetrahedral finite elements


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

		 method: "small", "large" (by QR), "polar" or "svd" displacements

		 poissonRatio: FEM Poisson Ratio in Hooke's law [0,0.5[

		 youngModulus: FEM Young's Modulus in Hooke's law

		 localStiffnessFactor: Allow specification of different stiffness per element. If there are N element and M values are specified, the youngModulus factor for element i would be localStiffnessFactor[i*M/N]

		 updateStiffnessMatrix: 

		 computeGlobalMatrix: 

		 plasticMaxThreshold: Plastic Max Threshold (2-norm of the strain)

		 plasticYieldThreshold: Plastic Yield Threshold (2-norm of the strain)

		 plasticCreep: Plastic Creep Factor * dt [0,1]. Warning this factor depends on dt.

		 gatherPt: number of dof accumulated per threads during the gather operation (Only use in GPU version)

		 gatherBsize: number of dof accumulated per threads during the gather operation (Only use in GPU version)

		 drawHeterogeneousTetra: Draw Heterogeneous Tetra in different color

		 computeVonMisesStress: compute and display von Mises stress: 0: no computations, 1: using corotational strain, 2: using full Green strain. Set listening=1

		 vonMisesPerElement: von Mises Stress per element

		 vonMisesPerNode: von Mises Stress per node

		 vonMisesStressColors: Vector of colors describing the VonMises stress

		 showStressColorMap: Color map used to show stress values

		 showStressAlpha: Alpha for vonMises visualisation

		 showVonMisesStressPerNode: draw points showing vonMises stress interpolated in nodes

		 showVonMisesStressPerElement: draw triangles showing vonMises stress interpolated in elements

		 updateStiffness: udpate structures (precomputed in init) using stiffness parameters in each iteration (set listening=1)


    """
    return attachedTo.createObject("TetrahedronFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, initialPoints=initialPoints, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, localStiffnessFactor=localStiffnessFactor, updateStiffnessMatrix=updateStiffnessMatrix, computeGlobalMatrix=computeGlobalMatrix, plasticMaxThreshold=plasticMaxThreshold, plasticYieldThreshold=plasticYieldThreshold, plasticCreep=plasticCreep, gatherPt=gatherPt, gatherBsize=gatherBsize, drawHeterogeneousTetra=drawHeterogeneousTetra, computeVonMisesStress=computeVonMisesStress, vonMisesPerElement=vonMisesPerElement, vonMisesPerNode=vonMisesPerNode, vonMisesStressColors=vonMisesStressColors, showStressColorMap=showStressColorMap, showStressAlpha=showStressAlpha, showVonMisesStressPerNode=showVonMisesStressPerNode, showVonMisesStressPerElement=showVonMisesStressPerElement, updateStiffness=updateStiffness, **kwargs)
