# -*- coding: utf-8 -*-


"""
Component TriangularQuadraticSpringsForceField

.. autofunction:: TriangularQuadraticSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangularQuadraticSpringsForceField(attachedTo , name='TriangularQuadraticSpringsForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, initialPoints=array([], shape=(0, 3), dtype=float64), poissonRatio=0.3, youngModulus=1000.0, dampingRatio=0.0, useAngularSprings=1, triangleInfo=[], edgeInfo=[], **kwargs):
    """Quadratic Springs on a Triangular Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 initialPoints: Initial Position

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young modulus in Hooke's law

		 dampingRatio: Ratio damping/stiffness

		 useAngularSprings: If Angular Springs should be used or not

		 triangleInfo: Internal triangle data

		 edgeInfo: Internal edge data


    """
    return attachedTo.createObject("TriangularQuadraticSpringsForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, initialPoints=initialPoints, poissonRatio=poissonRatio, youngModulus=youngModulus, dampingRatio=dampingRatio, useAngularSprings=useAngularSprings, triangleInfo=triangleInfo, edgeInfo=edgeInfo, **kwargs)
