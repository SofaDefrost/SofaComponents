# -*- coding: utf-8 -*-


"""
Component TriangularFEMForceFieldOptim

.. autofunction:: TriangularFEMForceFieldOptim

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangularFEMForceFieldOptim(attachedTo , poissonRatio, youngModulus, name='TriangularFEMForceFieldOptim', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, triangleInfo='', triangleState='', vertexInfo='', edgeInfo='', damping=0.0, restScale=1.0, showStressVector=0, showStressMaxValue=0.0, **kwargs):
    """Corotational Triangular finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 triangleInfo: Internal triangle data (persistent)

		 triangleState: Internal triangle data (time-dependent)

		 vertexInfo: Internal point data

		 edgeInfo: Internal edge data

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young modulus in Hooke's law

		 damping: Ratio damping/stiffness

		 restScale: Scale factor applied to rest positions (to simulate pre-stretched materials)

		 showStressVector: Flag activating rendering of stress directions within each triangle

		 showStressMaxValue: Max value for rendering of stress values


    """
    return attachedTo.createObject("TriangularFEMForceFieldOptim" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, triangleInfo=triangleInfo, triangleState=triangleState, vertexInfo=vertexInfo, edgeInfo=edgeInfo, poissonRatio=poissonRatio, youngModulus=youngModulus, damping=damping, restScale=restScale, showStressVector=showStressVector, showStressMaxValue=showStressMaxValue, **kwargs)
