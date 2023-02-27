# -*- coding: utf-8 -*-


"""
Component SurfacePressureForceField

.. autofunction:: SurfacePressureForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SurfacePressureForceField(attachedTo , name='SurfacePressureForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, pressure=0.0, min=array([0., 0., 0.]), max=array([0., 0., 0.]), triangleIndices=array([], dtype=int32), quadIndices=array([], dtype=int32), pulseMode=0, pressureLowerBound=0.0, pressureSpeed=0.0, volumeConservationMode=0, useTangentStiffness=1, defaultVolume=-1.0, mainDirection=array([0., 0., 0.]), drawForceScale=0.0, **kwargs):
    """SurfacePressure


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

		 min: Lower bond of the selection box

		 max: Upper bond of the selection box

		 triangleIndices: Indices of affected triangles

		 quadIndices: Indices of affected quads

		 pulseMode: Cyclic pressure application

		 pressureLowerBound: Pressure lower bound force per unit area (active in pulse mode)

		 pressureSpeed: Continuous pressure application in Pascal per second. Only active in pulse mode

		 volumeConservationMode: Pressure variation follow the inverse of the volume variation

		 useTangentStiffness: Whether (non-symmetric) stiffness matrix should be used

		 defaultVolume: Default Volume

		 mainDirection: Main direction for pressure application

		 drawForceScale: DEBUG: scale used to render force vectors


    """
    return attachedTo.createObject("SurfacePressureForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, pressure=pressure, min=min, max=max, triangleIndices=triangleIndices, quadIndices=quadIndices, pulseMode=pulseMode, pressureLowerBound=pressureLowerBound, pressureSpeed=pressureSpeed, volumeConservationMode=volumeConservationMode, useTangentStiffness=useTangentStiffness, defaultVolume=defaultVolume, mainDirection=mainDirection, drawForceScale=drawForceScale, **kwargs)
