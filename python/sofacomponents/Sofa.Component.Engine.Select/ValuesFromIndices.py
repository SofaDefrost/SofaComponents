# -*- coding: utf-8 -*-


"""
Component ValuesFromIndices

.. autofunction:: ValuesFromIndices

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ValuesFromIndices(attachedTo , name='ValuesFromIndices', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, indices=array([], dtype=int32), out=array([], shape=(0, 3), dtype=float64), outStr='', **kwargs):
    """Find the values given a list of indices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 in: input values (NB: use the kwargs syntax as name is a reserved word in python)

		 indices: Indices of the values

		 out: Output values corresponding to the indices

		 outStr: Output values corresponding to the indices, converted as a string


    """
    return attachedTo.createObject("ValuesFromIndices" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, indices=indices, out=out, outStr=outStr, **kwargs)
