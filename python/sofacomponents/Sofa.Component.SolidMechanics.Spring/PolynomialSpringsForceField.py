# -*- coding: utf-8 -*-


"""
Component PolynomialSpringsForceField

.. autofunction:: PolynomialSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PolynomialSpringsForceField(attachedTo , name='PolynomialSpringsForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, firstObjectPoints=array([], dtype=int32), secondObjectPoints=array([], dtype=int32), polynomialStiffness=array([], dtype=float64), polynomialDegree=array([], dtype=int32), computeZeroLength=1, zeroLength=array([], dtype=float64), recompute_indices=0, compressible=0, drawMode=0, showArrowSize=0.009999999776482582, springColor=array([0., 1., 0., 1.], dtype=float32), showIndicesScale=0.019999999552965164, **kwargs):
    """Simple elastic springs applied to given degrees of freedom between their current and rest shape position


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 firstObjectPoints: points related to the first object

		 secondObjectPoints: points related to the second object

		 polynomialStiffness: coefficients for all spring polynomials

		 polynomialDegree: vector of values that show polynomials degrees

		 computeZeroLength: flag to compute initial length for springs

		 zeroLength: initial length for springs

		 recompute_indices: Recompute indices (should be false for BBOX)

		 compressible: Indicates if object compresses without reactio force

		 drawMode: The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow

		 showArrowSize: size of the axis

		 springColor: spring color

		 showIndicesScale: Scale for indices display. (default=0.02)


    """
    return attachedTo.createObject("PolynomialSpringsForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, firstObjectPoints=firstObjectPoints, secondObjectPoints=secondObjectPoints, polynomialStiffness=polynomialStiffness, polynomialDegree=polynomialDegree, computeZeroLength=computeZeroLength, zeroLength=zeroLength, recompute_indices=recompute_indices, compressible=compressible, drawMode=drawMode, showArrowSize=showArrowSize, springColor=springColor, showIndicesScale=showIndicesScale, **kwargs)
