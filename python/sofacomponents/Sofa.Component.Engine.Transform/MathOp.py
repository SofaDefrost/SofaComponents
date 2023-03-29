# -*- coding: utf-8 -*-


"""
Component MathOp

.. autofunction:: MathOp

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MathOp(attachedTo , name='MathOp', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, nbInputs=2, op='+', output=array([], dtype=float64), input1=array([], dtype=float64), input2=array([], dtype=float64), **kwargs):
    """Apply a math operation to combine several inputs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 nbInputs: Number of input values

		 op: Selected operation to apply

		 output: Output values

		 input1: input values 1

		 input2: input values 2


    """
    return attachedTo.createObject("MathOp" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, nbInputs=nbInputs, op=op, output=output, input1=input1, input2=input2, **kwargs)
