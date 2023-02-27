# -*- coding: utf-8 -*-


"""
Component NormEngine

.. autofunction:: NormEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NormEngine(attachedTo , name='NormEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, input=array([], shape=(0, 3), dtype=float64), output=array([], dtype=float64), normType=2, **kwargs):
    """Convert Vec in Real


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 input: input array of 3d points

		 output: output array of scalar norms

		 normType: The type of norm. Use a negative value for the infinite norm.


    """
    return attachedTo.createObject("NormEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, input=input, output=output, normType=normType, **kwargs)
