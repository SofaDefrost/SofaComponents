# -*- coding: utf-8 -*-


"""
Component PolynomialRestShapeSpringsForceField

.. autofunction:: PolynomialRestShapeSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PolynomialRestShapeSpringsForceField(attachedTo , name='PolynomialRestShapeSpringsForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, points=array([], dtype=int32), external_points=array([], dtype=int32), polynomialStiffness=array([], dtype=float64), polynomialDegree=array([], dtype=int32), recompute_indices=0, drawSpring=0, springColor=array([0., 1., 0., 1.], dtype=float32), showIndicesScale=0.019999999552965164, initialLength=array([], dtype=float64), smoothShift=0.0, smoothScale=1.0, **kwargs):
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

		 points: points controlled by the rest shape springs

		 external_points: points from the external Mechancial State that define the rest shape springs

		 polynomialStiffness: coefficients for all spring polynomials

		 polynomialDegree: vector of values that show polynomials degrees

		 recompute_indices: Recompute indices (should be false for BBOX)

		 drawSpring: draw Spring

		 springColor: spring color

		 showIndicesScale: Scale for indices display. (default=0.02)

		 initialLength: initial virtual length of the spring

		 smoothShift: denominator correction adding shift value

		 smoothScale: denominator correction adding scale


    """
    return attachedTo.createObject("PolynomialRestShapeSpringsForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, points=points, external_points=external_points, polynomialStiffness=polynomialStiffness, polynomialDegree=polynomialDegree, recompute_indices=recompute_indices, drawSpring=drawSpring, springColor=springColor, showIndicesScale=showIndicesScale, initialLength=initialLength, smoothShift=smoothShift, smoothScale=smoothScale, **kwargs)
