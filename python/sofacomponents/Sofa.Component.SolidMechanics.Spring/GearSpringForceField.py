# -*- coding: utf-8 -*-


"""
Component GearSpringForceField

.. autofunction:: GearSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GearSpringForceField(attachedTo , name='GearSpringForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, spring=[], filename='', period=0.0, reinit=0, showFactorSize=1.0, **kwargs):
    """Gear springs for Rigids


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 spring: pairs of indices, stiffness, damping

		 filename: output file name

		 period: period between outputs

		 reinit: flag enabling reinitialization of the output file at each timestep

		 showFactorSize: modify the size of the debug information of a given factor


    """
    return attachedTo.createObject("GearSpringForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, spring=spring, filename=filename, period=period, reinit=reinit, showFactorSize=showFactorSize, **kwargs)
