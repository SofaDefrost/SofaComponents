# -*- coding: utf-8 -*-


"""
Component OscillatingTorsionPressureForceField

.. autofunction:: OscillatingTorsionPressureForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OscillatingTorsionPressureForceField(attachedTo , name='OscillatingTorsionPressureForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, trianglePressureMap='', moment=0.0, triangleList=[], axis=[[0.0, 0.0, 1.0]], center=[[0.0, 0.0, 0.0]], penalty=1000.0, frequency=1.0, dmin=0.0, dmax=0.0, showForces=0, **kwargs):
    """OscillatingTorsionPressure


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 trianglePressureMap: map between edge indices and their pressure

		 moment: Moment force applied on the entire surface

		 triangleList: Indices of triangles separated with commas where a pressure is applied

		 axis: Axis of rotation and normal direction for the plane selection of triangles

		 center: Center of rotation

		 penalty: Strength of the penalty force

		 frequency: frequency of oscillation

		 dmin: Minimum distance from the origin along the normal direction

		 dmax: Maximum distance from the origin along the normal direction

		 showForces: draw triangles which have a given pressure


    """
    return attachedTo.createObject("OscillatingTorsionPressureForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, trianglePressureMap=trianglePressureMap, moment=moment, triangleList=triangleList, axis=axis, center=center, penalty=penalty, frequency=frequency, dmin=dmin, dmax=dmax, showForces=showForces, **kwargs)
