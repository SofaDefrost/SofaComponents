# -*- coding: utf-8 -*-


"""
Component DiagonalMass

.. autofunction:: DiagonalMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DiagonalMass(attachedTo , name='DiagonalMass', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, vertexMass=array([], dtype=float64), massDensity=1.0, totalMass=1.0, computeMassOnRest=1, showGravityCenter=0, showAxisSizeFactor=1.0, filename='', **kwargs):
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

		 vertexMass: Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.

		 massDensity: Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.

		 totalMass: Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0

		 computeMassOnRest: If true, the mass of every element is computed based on the rest position rather than the position

		 showGravityCenter: Display the center of gravity of the system

		 showAxisSizeFactor: Factor length of the axis displayed (only used for rigids)

		 filename: Xsp3.0 file to specify the mass parameters


    """
    return attachedTo.createObject("DiagonalMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, vertexMass=vertexMass, massDensity=massDensity, totalMass=totalMass, computeMassOnRest=computeMassOnRest, showGravityCenter=showGravityCenter, showAxisSizeFactor=showAxisSizeFactor, filename=filename, **kwargs)
