# -*- coding: utf-8 -*-


"""
Component HexahedralFEMForceField

.. autofunction:: HexahedralFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HexahedralFEMForceField(attachedTo , poissonRatio, youngModulus, name='HexahedralFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, method='large', hexahedronInfo=[], **kwargs):
    """Hexahedral finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 method: "large" or "polar" displacements

		 poissonRatio: 

		 youngModulus: 

		 hexahedronInfo: Internal hexahedron data


    """
    return attachedTo.createObject("HexahedralFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, hexahedronInfo=hexahedronInfo, **kwargs)
