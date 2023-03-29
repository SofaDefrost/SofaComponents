# -*- coding: utf-8 -*-


"""
Component CholeskySolver

.. autofunction:: CholeskySolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CholeskySolver(attachedTo , name='CholeskySolver', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, verbose=0, **kwargs):
    """Direct linear solver based on Cholesky factorization, for dense matrices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 verbose: Dump system state at each iteration


    """
    return attachedTo.createObject("CholeskySolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, verbose=verbose, **kwargs)
