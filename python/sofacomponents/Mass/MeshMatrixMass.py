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

        
def MeshMatrixMass(attachedTo , name='MeshMatrixMass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, vertexMass=[], edgeMass=[], tetrahedronMass=[], massDensity=1.0, showGravityCenter=0, showAxisSizeFactor=1.0, lumping=1, printMass=0, graph='', integrationOrder=2, numericalIntegrationMethod=0, integrationMethod='analytical', **kwargs):
    """Define a specific mass for each particle


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

		 vertexMass: values of the particles masses on vertices

		 edgeMass: values of the particles masses on edges

		 tetrahedronMass: values of the particles masses for all control points inside a Bezier tetrahedron

		 massDensity: mass density that allows to compute the  particles masses from a mesh topology and geometry.
Only used if > 0

		 showGravityCenter: display the center of gravity of the system

		 showAxisSizeFactor: factor length of the axis displayed (only used for rigids)

		 lumping: boolean if you need to use a lumped mass matrix

		 printMass: boolean if you want to get the totalMass

		 graph: Graph of the controlled potential

		 integrationOrder: The order of integration for numerical integration

		 numericalIntegrationMethod: The type of numerical integration method chosen

		 integrationMethod: "exact" if closed form expression for high order elements, "analytical" if closed form expression for affine element, "numerical" if numerical integration is chosen


    """
    return attachedTo.createObject("MeshMatrixMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, vertexMass=vertexMass, edgeMass=edgeMass, tetrahedronMass=tetrahedronMass, massDensity=massDensity, showGravityCenter=showGravityCenter, showAxisSizeFactor=showAxisSizeFactor, lumping=lumping, printMass=printMass, graph=graph, integrationOrder=integrationOrder, numericalIntegrationMethod=numericalIntegrationMethod, integrationMethod=integrationMethod, **kwargs)
