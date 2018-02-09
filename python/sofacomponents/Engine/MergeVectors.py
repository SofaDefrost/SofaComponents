# -*- coding: utf-8 -*-


"""
Component MergeVectors

.. autofunction:: MergeVectors

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MergeVectors(attachedTo , name='MergeVectors', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, nbInputs=2, output=[], **kwargs):
    """Apply a merge operation to combine several inputs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 nbInputs: Number of input vectors

		 output: Output vector


    """
    return attachedTo.createObject("MergeVectors" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, nbInputs=nbInputs, output=output, **kwargs)
