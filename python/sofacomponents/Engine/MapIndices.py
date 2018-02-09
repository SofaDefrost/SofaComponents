# -*- coding: utf-8 -*-


"""
Component MapIndices

.. autofunction:: MapIndices

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MapIndices(attachedTo , name='MapIndices', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, indices=[], out=[], outStr='', transpose=0, **kwargs):
    """Apply a permutation to a set of indices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 in: input indices (NB: use the kwargs syntax as name is a reserved word in python)

		 indices: array containing in ith cell the input index corresponding to the output index i (or reversively if transpose=true)

		 out: Output indices

		 outStr: Output indices, converted as a string

		 transpose: Should the transposed mapping be used ?


    """
    return attachedTo.createObject("MapIndices" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, indices=indices, out=out, outStr=outStr, transpose=transpose, **kwargs)
