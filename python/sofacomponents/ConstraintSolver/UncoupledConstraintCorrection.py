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

        
def UncoupledConstraintCorrection(attachedTo , name='UncoupledConstraintCorrection', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, compliance=[], defaultCompliance=1e-05, verbose=0, handleTopologyChange=1, correctionVelocityFactor=1.0, correctionPositionFactor=1.0, useOdeSolverIntegrationFactors=0, **kwargs):
    """Component computing contact forces within a simulated body using the compliance method.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 compliance: compliance value on each dof

		 defaultCompliance: Default compliance value for new dof or if all should have the same (in which case compliance vector should be empty)

		 verbose: Dump the constraint matrix at each iteration

		 handleTopologyChange: Enable support of topological changes for compliance vector (disable if another component takes care of this)

		 correctionVelocityFactor: Factor applied to the constraint forces when correcting the velocities

		 correctionPositionFactor: Factor applied to the constraint forces when correcting the positions

		 useOdeSolverIntegrationFactors: Use odeSolver integration factors instead of correctionVelocityFactor and correctionPositionFactor


    """
    return attachedTo.createObject("UncoupledConstraintCorrection" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, compliance=compliance, defaultCompliance=defaultCompliance, verbose=verbose, handleTopologyChange=handleTopologyChange, correctionVelocityFactor=correctionVelocityFactor, correctionPositionFactor=correctionPositionFactor, useOdeSolverIntegrationFactors=useOdeSolverIntegrationFactors, **kwargs)
