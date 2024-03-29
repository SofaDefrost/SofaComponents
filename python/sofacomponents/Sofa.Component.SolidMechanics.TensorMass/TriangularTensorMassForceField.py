# -*- coding: utf-8 -*-


"""
Component TriangularTensorMassForceField

.. autofunction:: TriangularTensorMassForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangularTensorMassForceField(attachedTo , name='TriangularTensorMassForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, edgeInfo=[], poissonRatio=0.3, youngModulus=1000.0, **kwargs):
    """Linear Elastic Membrane on a Triangular Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 edgeInfo: Internal edge data

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young's modulus in Hooke's law


    """
    return attachedTo.createObject("TriangularTensorMassForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, edgeInfo=edgeInfo, poissonRatio=poissonRatio, youngModulus=youngModulus, **kwargs)
