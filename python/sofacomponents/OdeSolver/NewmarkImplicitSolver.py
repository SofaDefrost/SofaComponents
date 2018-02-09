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

        
def NewmarkImplicitSolver(attachedTo , name='NewmarkImplicitSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, rayleighStiffness=0.0, rayleighMass=0.0, vdamping=0.0, verbose=0, gamma=0.5, beta=0.25, **kwargs):
    """Implicit time integratorusing Newmark scheme


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 rayleighStiffness: Rayleigh damping coefficient related to stiffness

		 rayleighMass: Rayleigh damping coefficient related to mass

		 vdamping: Velocity decay coefficient (no decay if null)

		 verbose: Dump system state at each iteration

		 gamma: Newmark scheme gamma coefficient

		 beta: Newmark scheme beta coefficient


    """
    return attachedTo.createObject("NewmarkImplicitSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, rayleighStiffness=rayleighStiffness, rayleighMass=rayleighMass, vdamping=vdamping, verbose=verbose, gamma=gamma, beta=beta, **kwargs)
