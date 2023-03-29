# -*- coding: utf-8 -*-


"""
Component EulerExplicitSolver

.. autofunction:: EulerExplicitSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EulerExplicitSolver(attachedTo , name='EulerExplicitSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, symplectic=1, threadSafeVisitor=0, **kwargs):
    """A simple explicit time integrator


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 symplectic: If true, the velocities are updated before the positions and the method is symplectic (more robust). If false, the positions are updated before the velocities (standard Euler, less robust).

		 threadSafeVisitor: If true, do not use realloc and free visitors in fwdInteractionForceField.


    """
    return attachedTo.createObject("EulerExplicitSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, symplectic=symplectic, threadSafeVisitor=threadSafeVisitor, **kwargs)
