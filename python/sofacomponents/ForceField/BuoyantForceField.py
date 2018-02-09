# -*- coding: utf-8 -*-


"""
Component BuoyantForceField

.. autofunction:: BuoyantForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BuoyantForceField(attachedTo , name='BuoyantForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, fluidModel=1.0, min=[[-100.0, -100.0, -100.0]], max=[[100.0, 100.0, 0.0]], heightPlane=0.0, fluidDensity=1.0, fluidViscosity=0.001, atmosphericPressure=101325.0, enableViscosity=1, turbulentFlow=0, flipNormals=0, showPressureForces=0, showViscosityForces=0, showBoxOrPlane=0, showFactorSize=1.0, **kwargs):
    """Upward acting force exerted by a fluid, that opposes an object's weight


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 fluidModel: 1 for a plane, 2 for a box

		 min: Lower bound of the liquid box

		 max: Upper bound of the liquid box

		 heightPlane: height of the fluid orthogonal to the gravity

		 fluidDensity: Fluid Density

		 fluidViscosity: Fluid Viscosity

		 atmosphericPressure: atmospheric pressure

		 enableViscosity: enable the effects of viscosity

		 turbulentFlow: true for turbulent flow, false for laminar

		 flipNormals: flip normals to inverse the forces applied on the object

		 showPressureForces: Show the pressure forces applied on the surface of the mesh if true

		 showViscosityForces: Show the viscosity forces applied on the surface of the mesh if true

		 showBoxOrPlane: Show the box or the plane

		 showFactorSize: Size factor applied to shown forces


    """
    return attachedTo.createObject("BuoyantForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, fluidModel=fluidModel, min=min, max=max, heightPlane=heightPlane, fluidDensity=fluidDensity, fluidViscosity=fluidViscosity, atmosphericPressure=atmosphericPressure, enableViscosity=enableViscosity, turbulentFlow=turbulentFlow, flipNormals=flipNormals, showPressureForces=showPressureForces, showViscosityForces=showViscosityForces, showBoxOrPlane=showBoxOrPlane, showFactorSize=showFactorSize, **kwargs)
