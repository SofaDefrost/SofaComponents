# -*- coding: utf-8 -*-


"""
Component SubsetMapping

.. autofunction:: SubsetMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SubsetMapping(attachedTo , name='SubsetMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, indices=array([], dtype=int32), first=4294967295, last=4294967295, radius=1e-05, handleTopologyChange=1, ignoreNotFound=0, resizeToModel=0, **kwargs):
    """TODO-SubsetMappingClass


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 mapForces: Are forces mapped ?

		 mapConstraints: Are constraints mapped ?

		 mapMasses: Are masses mapped ?

		 mapMatrices: Are matrix explicit mapped?

		 applyRestPosition: set to true to apply this mapping to restPosition at init

		 indices: list of input indices

		 first: first index (use if indices are sequential)

		 last: last index (use if indices are sequential)

		 radius: search radius to find corresponding points in case no indices are given

		 handleTopologyChange: Enable support of topological changes for indices (disable if it is linked from SubsetTopologicalMapping::pointD2S)

		 ignoreNotFound: True to ignore points that are not found in the input model, they will be treated as fixed points

		 resizeToModel: True to resize the output MechanicalState to match the size of indices


    """
    return attachedTo.createObject("SubsetMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, indices=indices, first=first, last=last, radius=radius, handleTopologyChange=handleTopologyChange, ignoreNotFound=ignoreNotFound, resizeToModel=resizeToModel, **kwargs)
