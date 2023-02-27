# -*- coding: utf-8 -*-


"""
Component MergeSets

.. autofunction:: MergeSets

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MergeSets(attachedTo , name='MergeSets', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, in1=array([], dtype=int32), in2=array([], dtype=int32), out=array([], dtype=int32), op='union', **kwargs):
    """Merge two sets of indices using specified boolean operation


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 in1: first set of indices

		 in2: second set of indices

		 out: merged set of indices

		 op: name of operation to compute (union, intersection, difference, symmetric_difference)


    """
    return attachedTo.createObject("MergeSets" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, in1=in1, in2=in2, out=out, op=op, **kwargs)
