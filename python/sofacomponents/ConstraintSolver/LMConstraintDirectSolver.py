# -*- coding: utf-8 -*-


"""
Component LMConstraintDirectSolver

.. autofunction:: LMConstraintDirectSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LMConstraintDirectSolver(attachedTo , numIterations, maxError, name='LMConstraintDirectSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, constraintAcc=0, constraintVel=1, constraintPos=1, graphGSError='', traceKineticEnergy=0, graphKineticEnergy='', solverAlgorithm='SVD', **kwargs):
    """A Direct Constraint Solver working specifically with LMConstraint based components


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 constraintAcc: Constraint the acceleration

		 constraintVel: Constraint the velocity

		 constraintPos: Constraint the position

		 numIterations: Number of iterations for Gauss-Seidel when solving the Constraints

		 maxError: threshold for the residue of the Gauss-Seidel algorithm

		 graphGSError: Graph of residuals at each iteration

		 traceKineticEnergy: Trace the evolution of the Kinetic Energy throughout the solution of the system

		 graphKineticEnergy: Graph of the kinetic energy of the system

		 solverAlgorithm: Algorithm used to solve the system W.Lambda=c


    """
    return attachedTo.createObject("LMConstraintDirectSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, constraintAcc=constraintAcc, constraintVel=constraintVel, constraintPos=constraintPos, numIterations=numIterations, maxError=maxError, graphGSError=graphGSError, traceKineticEnergy=traceKineticEnergy, graphKineticEnergy=graphKineticEnergy, solverAlgorithm=solverAlgorithm, **kwargs)
