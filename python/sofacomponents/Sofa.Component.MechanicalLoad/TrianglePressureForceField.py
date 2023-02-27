# -*- coding: utf-8 -*-


"""
Component TrianglePressureForceField

.. autofunction:: TrianglePressureForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TrianglePressureForceField(attachedTo , name='TrianglePressureForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, pressure=array([0., 0., 0.]), cauchyStress='[ 0 0 0 , 0 0 0 , 0 0 0 ,]', triangleList=array([], dtype=int32), normal=array([0., 0., 0.]), dmin=0.0, dmax=0.0, showForces=0, useConstantForce=1, trianglePressureMap=[], **kwargs):
    """TrianglePressure


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 pressure: Pressure force per unit area

		 cauchyStress: Cauchy Stress applied on the normal of each triangle

		 triangleList: Indices of triangles separated with commas where a pressure is applied

		 normal: Normal direction for the plane selection of triangles

		 dmin: Minimum distance from the origin along the normal direction

		 dmax: Maximum distance from the origin along the normal direction

		 showForces: draw triangles which have a given pressure

		 useConstantForce: applied force is computed as the pressure vector times the area at rest

		 trianglePressureMap: map between edge indices and their pressure


    """
    return attachedTo.createObject("TrianglePressureForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, pressure=pressure, cauchyStress=cauchyStress, triangleList=triangleList, normal=normal, dmin=dmin, dmax=dmax, showForces=showForces, useConstantForce=useConstantForce, trianglePressureMap=trianglePressureMap, **kwargs)
