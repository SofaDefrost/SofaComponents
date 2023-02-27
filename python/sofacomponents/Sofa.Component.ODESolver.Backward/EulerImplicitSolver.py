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

        
def EulerImplicitSolver(attachedTo , name='EulerImplicitSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, rayleighStiffness=0.0, rayleighMass=0.0, vdamping=0.0, firstOrder=0, trapezoidalScheme=0, solveConstraint=0, threadSafeVisitor=0, **kwargs):
    """Time integrator using implicit backward Euler scheme


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 rayleighStiffness: Rayleigh damping coefficient related to stiffness, > 0

		 rayleighMass: Rayleigh damping coefficient related to mass, > 0

		 vdamping: Velocity decay coefficient (no decay if null)

		 firstOrder: Use backward Euler scheme for first order ode system.

		 trapezoidalScheme: Optional: use the trapezoidal scheme instead of the implicit Euler scheme and get second order accuracy in time

		 solveConstraint: Apply ConstraintSolver (requires a ConstraintSolver in the same node as this solver, disabled by by default for now)

		 threadSafeVisitor: If true, do not use realloc and free visitors in fwdInteractionForceField.


    """
    return attachedTo.createObject("EulerImplicitSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, rayleighStiffness=rayleighStiffness, rayleighMass=rayleighMass, vdamping=vdamping, firstOrder=firstOrder, trapezoidalScheme=trapezoidalScheme, solveConstraint=solveConstraint, threadSafeVisitor=threadSafeVisitor, **kwargs)
