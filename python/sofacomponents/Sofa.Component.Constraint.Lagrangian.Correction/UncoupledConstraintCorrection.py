# -*- coding: utf-8 -*-


"""
Component UncoupledConstraintCorrection

.. autofunction:: UncoupledConstraintCorrection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def UncoupledConstraintCorrection(attachedTo , name='UncoupledConstraintCorrection', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, compliance=array([], dtype=float64), defaultCompliance=1e-05, verbose=0, correctionVelocityFactor=1.0, correctionPositionFactor=1.0, useOdeSolverIntegrationFactors=1, **kwargs):
    """Component computing constraint forces within a simulated body using the compliance method.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 compliance: compliance value on each dof. If Rigid compliance (7 values): 1st value for translations, 6 others for upper-triangular part of symmetric 3x3 rotation compliance matrix

		 defaultCompliance: Default compliance value for new dof or if all should have the same (in which case compliance vector should be empty)

		 verbose: Dump the constraint matrix at each iteration

		 correctionVelocityFactor: Factor applied to the constraint forces when correcting the velocities

		 correctionPositionFactor: Factor applied to the constraint forces when correcting the positions

		 useOdeSolverIntegrationFactors: Use odeSolver integration factors instead of correctionVelocityFactor and correctionPositionFactor


    """
    return attachedTo.createObject("UncoupledConstraintCorrection" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, compliance=compliance, defaultCompliance=defaultCompliance, verbose=verbose, correctionVelocityFactor=correctionVelocityFactor, correctionPositionFactor=correctionPositionFactor, useOdeSolverIntegrationFactors=useOdeSolverIntegrationFactors, **kwargs)
