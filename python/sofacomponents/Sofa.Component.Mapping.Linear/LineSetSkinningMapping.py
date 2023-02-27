# -*- coding: utf-8 -*-


"""
Component LineSetSkinningMapping

.. autofunction:: LineSetSkinningMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LineSetSkinningMapping(attachedTo , name='LineSetSkinningMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, neighborhoodLevel=3, numberInfluencedLines=4, weightCoef=4, **kwargs):
    """skin a model from a set of rigid lines


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

		 neighborhoodLevel: Set the neighborhood line level

		 numberInfluencedLines: Set the number of most influenced lines by each vertice

		 weightCoef: Set the coefficient used to compute the weight of lines


    """
    return attachedTo.createObject("LineSetSkinningMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, neighborhoodLevel=neighborhoodLevel, numberInfluencedLines=numberInfluencedLines, weightCoef=weightCoef, **kwargs)
