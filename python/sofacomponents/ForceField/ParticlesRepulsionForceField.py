# -*- coding: utf-8 -*-


"""
Component ParticlesRepulsionForceField

.. autofunction:: ParticlesRepulsionForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ParticlesRepulsionForceField(attachedTo , name='ParticlesRepulsionForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, distance=1.0, stiffness=100.0, damping=0.1, **kwargs):
    """ForceField using SpatialGridContainer to compute repulsion forces in a set of spheres


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 distance: Distance to maintain between particles

		 stiffness: Stiffness

		 damping: Damping


    """
    return attachedTo.createObject("ParticlesRepulsionForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, distance=distance, stiffness=stiffness, damping=damping, **kwargs)
