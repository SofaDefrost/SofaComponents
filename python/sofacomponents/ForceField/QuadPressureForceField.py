# -*- coding: utf-8 -*-


"""
Component QuadPressureForceField

.. autofunction:: QuadPressureForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def QuadPressureForceField(attachedTo , name='QuadPressureForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, pressure=[[0.0, 0.0, 0.0]], quadList=[], normal=[[0.0, 0.0, 0.0]], dmin=0.0, dmax=0.0, showForces=0, quadPressureMap='', **kwargs):
    """QuadPressure


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 pressure: Pressure force per unit area

		 quadList: Indices of quads separated with commas where a pressure is applied

		 normal: Normal direction for the plane selection of quads

		 dmin: Minimum distance from the origin along the normal direction

		 dmax: Maximum distance from the origin along the normal direction

		 showForces: draw quads which have a given pressure

		 quadPressureMap: map between edge indices and their pressure


    """
    return attachedTo.createObject("QuadPressureForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, pressure=pressure, quadList=quadList, normal=normal, dmin=dmin, dmax=dmax, showForces=showForces, quadPressureMap=quadPressureMap, **kwargs)
