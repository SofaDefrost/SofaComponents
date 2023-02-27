# -*- coding: utf-8 -*-


"""
Component BTDLinearSolver

.. autofunction:: BTDLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BTDLinearSolver(attachedTo , name='BTDLinearSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, verbose=0, showProblem=0, subpartSolve=0, verification=0, **kwargs):
    """Linear system solver using Thomas Algorithm for Block Tridiagonal matrices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 verbose: Dump system state at each iteration

		 showProblem: display debug informations about subpartSolve computation

		 subpartSolve: Allows for the computation of a subpart of the system

		 verification: verification of the subpartSolve


    """
    return attachedTo.createObject("BTDLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, verbose=verbose, showProblem=showProblem, subpartSolve=subpartSolve, verification=verification, **kwargs)
