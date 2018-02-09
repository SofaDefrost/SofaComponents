# -*- coding: utf-8 -*-


"""
Component UniformMass

.. autofunction:: UniformMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def UniformMass(attachedTo , name='UniformMass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, mass=1.0, totalmass=0.0, filename='unused', showGravityCenter=0, showAxisSizeFactor=1.0, compute_mapping_inertia=0, showInitialCenterOfGravity=0, showX0=0, localRange=[[-1, -1]], indices=[], handleTopoChange=0, preserveTotalMass=0, **kwargs):
    """Define the same mass for all the particles


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

		 mass: Specify a unique mass for all the particles.                      If the mass attribute is set then totalmass is deduced from it     using the following formula: totalmass = mass * number of particulesThe default value is {1.0}

		 totalmass: Specify a unique mass for all the particles.                        If the totalmass attribute is set then the mass is deduced from it   using the following formula: mass = totalmass / number of particules If unspecified the default value is totalmass = mass * number of particules.

		 filename: File storing the mass parameters [rigid objects only].

		 showGravityCenter: display the center of gravity of the system

		 showAxisSizeFactor: factor length of the axis displayed (only used for rigids)

		 compute_mapping_inertia: to be used if the mass is placed under a mapping

		 showInitialCenterOfGravity: display the initial center of gravity of the system

		 showX0: display the rest positions

		 localRange: optional range of local DOF indices. 
Any computation involving only indices outside of this range 
are discarded (useful for parallelization using mesh partitionning)

		 indices: optional local DOF indices. Any computation involving only indices outside of this list are discarded

		 handleTopoChange: The mass and totalMass are recomputed on particles add/remove.

		 preserveTotalMass: Prevent totalMass from decreasing when removing particles.


    """
    return attachedTo.createObject("UniformMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, mass=mass, totalmass=totalmass, filename=filename, showGravityCenter=showGravityCenter, showAxisSizeFactor=showAxisSizeFactor, compute_mapping_inertia=compute_mapping_inertia, showInitialCenterOfGravity=showInitialCenterOfGravity, showX0=showX0, localRange=localRange, indices=indices, handleTopoChange=handleTopoChange, preserveTotalMass=preserveTotalMass, **kwargs)
