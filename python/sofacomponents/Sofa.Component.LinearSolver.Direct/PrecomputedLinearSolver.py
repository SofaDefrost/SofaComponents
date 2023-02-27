# -*- coding: utf-8 -*-


"""
Component PrecomputedLinearSolver

.. autofunction:: PrecomputedLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PrecomputedLinearSolver(attachedTo , name='PrecomputedLinearSolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, jmjt_twostep=1, verbose=0, use_file=1, **kwargs):
    """Linear system solver based on a precomputed inverse matrix


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 jmjt_twostep: Use two step algorithm to compute JMinvJt

		 verbose: Dump system state at each iteration

		 use_file: Dump system matrix in a file


    """
    return attachedTo.createObject("PrecomputedLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, jmjt_twostep=jmjt_twostep, verbose=verbose, use_file=use_file, **kwargs)
