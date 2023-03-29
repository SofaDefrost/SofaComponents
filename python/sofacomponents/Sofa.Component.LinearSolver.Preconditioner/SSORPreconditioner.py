# -*- coding: utf-8 -*-


"""
Component SSORPreconditioner

.. autofunction:: SSORPreconditioner

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SSORPreconditioner(attachedTo , name='SSORPreconditioner', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, verbose=0, omega=1.0, **kwargs):
    """Linear system solver / preconditioner based on Symmetric Successive Over-Relaxation (SSOR). If the matrix is decomposed as $A = D + L + L^T$, this solver computes $(1/(2-w))(D/w+L)(D/w)^{-1}(D/w+L)^T x = b, or $(D+L)D^{-1}(D+L)^T x = b$ if $w=1$.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 verbose: Dump system state at each iteration

		 omega: Omega coefficient


    """
    return attachedTo.createObject("SSORPreconditioner" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, verbose=verbose, omega=omega, **kwargs)
