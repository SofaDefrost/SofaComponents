# -*- coding: utf-8 -*-


"""
Component TetrahedralTensorMassForceField

.. autofunction:: TetrahedralTensorMassForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedralTensorMassForceField(attachedTo , name='TetrahedralTensorMassForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, poissonRatio=0.3, youngModulus=1000.0, edgeInfo='', **kwargs):
    """Linear Elastic Tetrahedral Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young modulus in Hooke's law

		 edgeInfo: Internal edge data


    """
    return attachedTo.createObject("TetrahedralTensorMassForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, poissonRatio=poissonRatio, youngModulus=youngModulus, edgeInfo=edgeInfo, **kwargs)
