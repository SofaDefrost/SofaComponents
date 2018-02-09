# -*- coding: utf-8 -*-


"""
Component DifferenceEngine

.. autofunction:: DifferenceEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DifferenceEngine(attachedTo , name='DifferenceEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, input=[], substractor=[], output=[], **kwargs):
    """Computing the difference between two vector of dofs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 input: input vector

		 substractor: vector to substract to input

		 output: output vector = input-substractor


    """
    return attachedTo.createObject("DifferenceEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, input=input, substractor=substractor, output=output, **kwargs)
