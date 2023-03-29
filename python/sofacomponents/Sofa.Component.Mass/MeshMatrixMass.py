# -*- coding: utf-8 -*-


"""
Component MeshMatrixMass

.. autofunction:: MeshMatrixMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshMatrixMass(attachedTo , name='MeshMatrixMass', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, massDensity=array([], dtype=float64), totalMass=1.0, vertexMass=array([], dtype=float64), edgeMass=array([], dtype=float64), computeMassOnRest=0, showGravityCenter=0, showAxisSizeFactor=1.0, lumping=0, printMass=0, graph='', **kwargs):
    """Define a specific mass for each particle


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 separateGravity: add separately gravity to velocity computation

		 rayleighMass: Rayleigh damping - mass matrix coefficient

		 massDensity: Specify real and strictly positive value(s) for the mass density. 
If unspecified or wrongly set, the totalMass information is used.

		 totalMass: Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0

		 vertexMass: internal values of the particles masses on vertices, supporting topological changes

		 edgeMass: internal values of the particles masses on edges, supporting topological changes

		 computeMassOnRest: If true, the mass of every element is computed based on the rest position rather than the position

		 showGravityCenter: display the center of gravity of the system

		 showAxisSizeFactor: factor length of the axis displayed (only used for rigids)

		 lumping: boolean if you need to use a lumped mass matrix

		 printMass: boolean if you want to check the mass conservation

		 graph: Graph of the controlled potential


    """
    return attachedTo.createObject("MeshMatrixMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, massDensity=massDensity, totalMass=totalMass, vertexMass=vertexMass, edgeMass=edgeMass, computeMassOnRest=computeMassOnRest, showGravityCenter=showGravityCenter, showAxisSizeFactor=showAxisSizeFactor, lumping=lumping, printMass=printMass, graph=graph, **kwargs)
