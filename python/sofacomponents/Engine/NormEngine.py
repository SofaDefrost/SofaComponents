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

        
def NormEngine(attachedTo , name='NormEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, input=[], output=[], normType=2, **kwargs):
    """Convert Vec in Real


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 input: input array of 3d points

		 output: output array of scalar norms

		 normType: The type of norm. Use a negative value for the infinite norm.


    """
    return attachedTo.createObject("NormEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, input=input, output=output, normType=normType, **kwargs)
