# -*- coding: utf-8 -*-


"""
Component SPHFluidForceField

.. autofunction:: SPHFluidForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SPHFluidForceField(attachedTo , name='SPHFluidForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, radius=1.0, mass=1.0, pressure=100.0, density=1.0, viscosity=0.0010000000474974513, surfaceTension=0.0, kernelType=0, pressureType=1, viscosityType=1, surfaceTensionType=1, **kwargs):
    """Smooth Particle Hydrodynamics


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 radius: Radius of a Particle

		 mass: Mass of a Particle

		 pressure: Pressure

		 density: Density

		 viscosity: Viscosity

		 surfaceTension: Surface Tension

		 kernelType: 0 = default kernels, 1 = cubic spline

		 pressureType: 0 = none, 1 = default pressure

		 viscosityType: 0 = none, 1 = default viscosity using kernel Laplacian, 2 = artificial viscosity

		 surfaceTensionType: 0 = none, 1 = default surface tension using kernel Laplacian, 2 = cohesion forces surface tension from Becker et al. 2007


    """
    return attachedTo.createObject("SPHFluidForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, radius=radius, mass=mass, pressure=pressure, density=density, viscosity=viscosity, surfaceTension=surfaceTension, kernelType=kernelType, pressureType=pressureType, viscosityType=viscosityType, surfaceTensionType=surfaceTensionType, **kwargs)
