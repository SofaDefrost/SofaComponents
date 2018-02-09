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

        
def MathOp(attachedTo , name='MathOp', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, nbInputs=2, op='+', output=[], input1=[], input2=[], **kwargs):
    """Apply a math operation to combine several inputs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 nbInputs: Number of input values

		 op: Selected operation to apply

		 output: Output values

		 input1: 

		 input2: 


    """
    return attachedTo.createObject("MathOp" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, nbInputs=nbInputs, op=op, output=output, input1=input1, input2=input2, **kwargs)
