# -*- coding: utf-8 -*-


"""
Component LinearForceField

.. autofunction:: LinearForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LinearForceField(attachedTo , name='LinearForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, points=array([], dtype=int32), force=1.0, times=array([], dtype=float64), forces=array([], shape=(0, 3), dtype=float64), arrowSizeCoef=0.0, **kwargs):
    """Linearly interpolated force applied to given degrees of freedom


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 points: points where the force is applied

		 force: applied force to all points

		 times: key times for the interpolation

		 forces: forces corresponding to the key times

		 arrowSizeCoef: Size of the drawn arrows (0->no arrows, sign->direction of drawing


    """
    return attachedTo.createObject("LinearForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, points=points, force=force, times=times, forces=forces, arrowSizeCoef=arrowSizeCoef, **kwargs)
