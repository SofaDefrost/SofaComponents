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

        
def DiagonalMass(attachedTo , name='DiagonalMass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, mass=[], massDensity=1.0, computeMassOnRest=0, totalMass=-1.0, showGravityCenter=0, showAxisSizeFactor=1.0, fileMass='', **kwargs):
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

		 mass: values of the particles masses

		 massDensity: mass density that allows to compute the  particles masses from a mesh topology and geometry.
Only used if > 0

		 computeMassOnRest: if true, the mass of every element is computed based on the rest position rather than the position

		 totalMass: Total mass of the object, if set, the massDensity is overwritten

		 showGravityCenter: display the center of gravity of the system

		 showAxisSizeFactor: factor length of the axis displayed (only used for rigids)

		 fileMass: an Xsp3.0 file to specify the mass parameters


    """
    return attachedTo.createObject("DiagonalMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, mass=mass, massDensity=massDensity, computeMassOnRest=computeMassOnRest, totalMass=totalMass, showGravityCenter=showGravityCenter, showAxisSizeFactor=showAxisSizeFactor, fileMass=fileMass, **kwargs)
