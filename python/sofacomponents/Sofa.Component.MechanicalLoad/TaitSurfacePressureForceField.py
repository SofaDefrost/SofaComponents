# -*- coding: utf-8 -*-


"""
Component TaitSurfacePressureForceField

.. autofunction:: TaitSurfacePressureForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TaitSurfacePressureForceField(attachedTo , name='TaitSurfacePressureForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, isCompliance=0, rayleighStiffness=0.0, p0=0.0, B=0.0, gamma=0.0, injectedVolume=0.0, maxInjectionRate=1000.0, initialVolume=0.0, currentInjectedVolume=0.0, v0=0.0, currentVolume=0.0, currentPressure=0.0, currentStiffness=0.0, pressureTriangles=array([], shape=(0, 3), dtype=int32), initialSurfaceArea=0.0, currentSurfaceArea=0.0, drawForceScale=0.001, drawForceColor=array([0., 1., 1., 1.], dtype=float32), volumeAfterTC=0.0, surfaceAreaAfterTC=0.0, **kwargs):
    """This component computes the volume enclosed by a surface mesh and apply a pressure force following Tait's equation: $P = P_0 - B((V/V_0)^\gamma - 1)$.
This ForceField can be used to apply :
 * a constant pressure (set $B=0$ and use $P_0$)
 * an ideal gas pressure (set $\gamma=1$ and use $B$)
 * a pressure from water (set $\gamma=7$ and use $B$)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 p0: IN: Rest pressure when V = V0

		 B: IN: Bulk modulus (resistance to uniform compression)

		 gamma: IN: Bulk modulus (resistance to uniform compression)

		 injectedVolume: IN: Injected (or extracted) volume since the start of the simulation

		 maxInjectionRate: IN: Maximum injection rate (volume per second)

		 initialVolume: OUT: Initial volume, as computed from the surface rest position

		 currentInjectedVolume: OUT: Current injected (or extracted) volume (taking into account maxInjectionRate)

		 v0: OUT: Rest volume (as computed from initialVolume + injectedVolume)

		 currentVolume: OUT: Current volume, as computed from the last surface position

		 currentPressure: OUT: Current pressure, as computed from the last surface position

		 currentStiffness: OUT: dP/dV at current volume and pressure

		 pressureTriangles: OUT: list of triangles where a pressure is applied (mesh triangles + tesselated quads)

		 initialSurfaceArea: OUT: Initial surface area, as computed from the surface rest position

		 currentSurfaceArea: OUT: Current surface area, as computed from the last surface position

		 drawForceScale: DEBUG: scale used to render force vectors

		 drawForceColor: DEBUG: color used to render force vectors

		 volumeAfterTC: OUT: Volume after a topology change

		 surfaceAreaAfterTC: OUT: Surface area after a topology change


    """
    return attachedTo.createObject("TaitSurfacePressureForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, p0=p0, B=B, gamma=gamma, injectedVolume=injectedVolume, maxInjectionRate=maxInjectionRate, initialVolume=initialVolume, currentInjectedVolume=currentInjectedVolume, v0=v0, currentVolume=currentVolume, currentPressure=currentPressure, currentStiffness=currentStiffness, pressureTriangles=pressureTriangles, initialSurfaceArea=initialSurfaceArea, currentSurfaceArea=currentSurfaceArea, drawForceScale=drawForceScale, drawForceColor=drawForceColor, volumeAfterTC=volumeAfterTC, surfaceAreaAfterTC=surfaceAreaAfterTC, **kwargs)
