# -*- coding: utf-8 -*-


"""
Component BeamFEMForceField

.. autofunction:: BeamFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BeamFEMForceField(attachedTo , poissonRatio, name='BeamFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, beamsData=[], youngModulus=5000.0, radius=0.1, radiusInner=0.0, listSegment=array([], dtype=int32), useSymmetricAssembly=0, **kwargs):
    """Beam finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 beamsData: Internal element data

		 poissonRatio: Poisson's Ratio

		 youngModulus: Young Modulus

		 radius: radius of the section

		 radiusInner: inner radius of the section for hollow beams

		 listSegment: apply the forcefield to a subset list of beam segments. If no segment defined, forcefield applies to the whole topology

		 useSymmetricAssembly: use symmetric assembly of the matrix K


    """
    return attachedTo.createObject("BeamFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, beamsData=beamsData, poissonRatio=poissonRatio, youngModulus=youngModulus, radius=radius, radiusInner=radiusInner, listSegment=listSegment, useSymmetricAssembly=useSymmetricAssembly, **kwargs)
