# -*- coding: utf-8 -*-


"""
Component EulerImplicitSolver

.. autofunction:: EulerImplicitSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EulerImplicitSolver(attachedTo , name='EulerImplicitSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, rayleighStiffness=0.0, rayleighMass=0.0, vdamping=0.0, firstOrder=0, verbose=0, trapezoidalScheme=0, solveConstraint=0, **kwargs):
    """Time integrator using implicit backward Euler scheme


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 rayleighStiffness: Rayleigh damping coefficient related to stiffness, > 0

		 rayleighMass: Rayleigh damping coefficient related to mass, > 0

		 vdamping: Velocity decay coefficient (no decay if null)

		 firstOrder: Use backward Euler scheme for first order ode system.

		 verbose: Dump system state at each iteration

		 trapezoidalScheme: Optional: use the trapezoidal scheme instead of the implicit Euler scheme and get second order accuracy in time

		 solveConstraint: Apply ConstraintSolver (requires a ConstraintSolver in the same node as this solver, disabled by by default for now)


    """
    return attachedTo.createObject("EulerImplicitSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, rayleighStiffness=rayleighStiffness, rayleighMass=rayleighMass, vdamping=vdamping, firstOrder=firstOrder, verbose=verbose, trapezoidalScheme=trapezoidalScheme, solveConstraint=solveConstraint, **kwargs)
