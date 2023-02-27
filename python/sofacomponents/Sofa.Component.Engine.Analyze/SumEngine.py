# -*- coding: utf-8 -*-


"""
Component SumEngine

.. autofunction:: SumEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SumEngine(attachedTo , name='SumEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, input=array([], shape=(0, 3), dtype=float64), output=array([0., 0., 0.]), **kwargs):
    """Computing the Sum between two vector of dofs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 input: input vector

		 output: output sum


    """
    return attachedTo.createObject("SumEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, input=input, output=output, **kwargs)
