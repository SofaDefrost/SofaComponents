# -*- coding: utf-8 -*-


"""
Component NewmarkImplicitSolver

.. autofunction:: NewmarkImplicitSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NewmarkImplicitSolver(attachedTo , name='NewmarkImplicitSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, rayleighStiffness=0.0, rayleighMass=0.0, vdamping=0.0, gamma=0.5, beta=0.25, threadSafeVisitor=0, **kwargs):
    """Implicit time integrator using Newmark scheme


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 rayleighStiffness: Rayleigh damping coefficient related to stiffness

		 rayleighMass: Rayleigh damping coefficient related to mass

		 vdamping: Velocity decay coefficient (no decay if null)

		 gamma: Newmark scheme gamma coefficient

		 beta: Newmark scheme beta coefficient

		 threadSafeVisitor: If true, do not use realloc and free visitors in fwdInteractionForceField.


    """
    return attachedTo.createObject("NewmarkImplicitSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, rayleighStiffness=rayleighStiffness, rayleighMass=rayleighMass, vdamping=vdamping, gamma=gamma, beta=beta, threadSafeVisitor=threadSafeVisitor, **kwargs)
