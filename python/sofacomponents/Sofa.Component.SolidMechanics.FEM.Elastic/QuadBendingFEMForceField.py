# -*- coding: utf-8 -*-


"""
Component QuadBendingFEMForceField

.. autofunction:: QuadBendingFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def QuadBendingFEMForceField(attachedTo , name='QuadBendingFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, quadInfo=[], vertexInfo=[], edgeInfo=[], method='small', poissonRatio=array([0.45]), youngModulus=array([1000.]), thickness=1.0, **kwargs):
    """Bending Quad finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 quadInfo: Internal quad data

		 vertexInfo: Internal node data

		 edgeInfo: Internal edge data

		 method: large: large displacements, small: small displacements

		 poissonRatio: Poisson ratio in Hooke's law (vector)

		 youngModulus: Young modulus in Hooke's law (vector)

		 thickness: Thickness of the elements


    """
    return attachedTo.createObject("QuadBendingFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, quadInfo=quadInfo, vertexInfo=vertexInfo, edgeInfo=edgeInfo, method=method, poissonRatio=poissonRatio, youngModulus=youngModulus, thickness=thickness, **kwargs)
