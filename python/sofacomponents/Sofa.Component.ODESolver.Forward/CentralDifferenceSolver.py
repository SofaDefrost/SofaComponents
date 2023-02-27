# -*- coding: utf-8 -*-


"""
Component CentralDifferenceSolver

.. autofunction:: CentralDifferenceSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CentralDifferenceSolver(attachedTo , name='CentralDifferenceSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, rayleighMass=0.0, threadSafeVisitor=0, **kwargs):
    """Explicit time integrator using central difference (also known as Verlet of Leap-frog)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 rayleighMass: Rayleigh damping coefficient related to mass

		 threadSafeVisitor: If true, do not use realloc and free visitors in fwdInteractionForceField.


    """
    return attachedTo.createObject("CentralDifferenceSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, rayleighMass=rayleighMass, threadSafeVisitor=threadSafeVisitor, **kwargs)
