# -*- coding: utf-8 -*-


"""
Component EdgePressureForceField

.. autofunction:: EdgePressureForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EdgePressureForceField(attachedTo , name='EdgePressureForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, edgePressureMap='', pressure=[[0.0, 0.0, 0.0]], edgeIndices=[], edges=[], normal=[[0.0, 0.0, 0.0]], dmin=0.0, dmax=0.0, arrowSizeCoef=0.0, p_intensity=[], binormal=[[0.0, 0.0, 0.0]], showForces=0, **kwargs):
    """EdgePressure


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 edgePressureMap: map between edge indices and their pressure

		 pressure: Pressure force per unit area

		 edgeIndices: Indices of edges separated with commas where a pressure is applied

		 edges: List of edges where a pressure is applied

		 normal: Normal direction for the plane selection of edges

		 dmin: Minimum distance from the origin along the normal direction

		 dmax: Maximum distance from the origin along the normal direction

		 arrowSizeCoef: Size of the drawn arrows (0->no arrows, sign->direction of drawing

		 p_intensity: pressure intensity on edge normal

		 binormal: Binormal of the 2D plane

		 showForces: draw arrows of edge pressures


    """
    return attachedTo.createObject("EdgePressureForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, edgePressureMap=edgePressureMap, pressure=pressure, edgeIndices=edgeIndices, edges=edges, normal=normal, dmin=dmin, dmax=dmax, arrowSizeCoef=arrowSizeCoef, p_intensity=p_intensity, binormal=binormal, showForces=showForces, **kwargs)
