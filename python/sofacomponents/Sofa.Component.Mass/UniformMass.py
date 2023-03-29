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

        
def UniformMass(attachedTo , name='UniformMass', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, separateGravity=0, rayleighMass=0.0, vertexMass=1.0, totalMass=1.0, filename='unused', showGravityCenter=0, showAxisSizeFactor=1.0, compute_mapping_inertia=0, showInitialCenterOfGravity=0, showX0=0, localRange=array([-1, -1], dtype=int32), indices=array([], dtype=int32), preserveTotalMass=0, **kwargs):
    """Define the same mass for all the particles


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

		 vertexMass: Specify one single, positive, real value for the mass of each particle. 
If unspecified or wrongly set, the totalMass information is used.

		 totalMass: Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0

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

		 preserveTotalMass: Prevent totalMass from decreasing when removing particles.


    """
    return attachedTo.createObject("UniformMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, separateGravity=separateGravity, rayleighMass=rayleighMass, vertexMass=vertexMass, totalMass=totalMass, filename=filename, showGravityCenter=showGravityCenter, showAxisSizeFactor=showAxisSizeFactor, compute_mapping_inertia=compute_mapping_inertia, showInitialCenterOfGravity=showInitialCenterOfGravity, showX0=showX0, localRange=localRange, indices=indices, preserveTotalMass=preserveTotalMass, **kwargs)
