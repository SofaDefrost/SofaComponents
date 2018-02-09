# -*- coding: utf-8 -*-


"""
Component IndicesFromValues

.. autofunction:: IndicesFromValues

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def IndicesFromValues(attachedTo , name='IndicesFromValues', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, values=[], indices=[], otherIndices=[], recursiveSearch=0, **kwargs):
    """Find the indices of a list of values within a larger set of values


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 values: input values

		 global: Global values, in which the input values are searched (NB: use the kwargs syntax as name is a reserved word in python)

		 indices: Output indices of the given values, searched in global

		 otherIndices: Output indices of the other values, (NOT the given ones) searched in global

		 recursiveSearch: if set to true, output are indices of the "global" data matching with one of the values


    """
    return attachedTo.createObject("IndicesFromValues" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, values=values, indices=indices, otherIndices=otherIndices, recursiveSearch=recursiveSearch, **kwargs)
