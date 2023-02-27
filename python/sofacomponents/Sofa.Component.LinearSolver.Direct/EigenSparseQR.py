# -*- coding: utf-8 -*-


"""
Component EigenSparseQR

.. autofunction:: EigenSparseQR

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EigenSparseQR(attachedTo , name='EigenSparseQR', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, ordering='AMD', **kwargs):
    """Direct Linear Solver using a Sparse QR factorization.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 ordering: Ordering method


    """
    return attachedTo.createObject("EigenSparseQR" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, ordering=ordering, **kwargs)
