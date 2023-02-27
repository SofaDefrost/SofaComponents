# -*- coding: utf-8 -*-


"""
Component TriangularBiquadraticSpringsForceField

.. autofunction:: TriangularBiquadraticSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangularBiquadraticSpringsForceField(attachedTo , name='TriangularBiquadraticSpringsForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, triangleInfo=[], edgeInfo=[], initialPoints=array([], shape=(0, 3), dtype=float64), poissonRatio=0.3, youngModulus=1000.0, dampingRatio=0.0, useAngularSprings=1, compressible=1, matrixRegularization=0.4, **kwargs):
    """Biquadratic Springs on a Triangular Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 triangleInfo: Internal triangle data

		 edgeInfo: Internal edge data

		 initialPoints: Initial Position

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young modulus in Hooke's law

		 dampingRatio: Ratio damping/stiffness

		 useAngularSprings: If Angular Springs should be used or not

		 compressible: If additional energy penalizing compressibility should be used

		 matrixRegularization: Regularization of the Stiffnes Matrix (between 0 and 1)


    """
    return attachedTo.createObject("TriangularBiquadraticSpringsForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, triangleInfo=triangleInfo, edgeInfo=edgeInfo, initialPoints=initialPoints, poissonRatio=poissonRatio, youngModulus=youngModulus, dampingRatio=dampingRatio, useAngularSprings=useAngularSprings, compressible=compressible, matrixRegularization=matrixRegularization, **kwargs)
