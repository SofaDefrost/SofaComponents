# -*- coding: utf-8 -*-


"""
Component SkinningMapping

.. autofunction:: SkinningMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SkinningMapping(attachedTo , name='SkinningMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, initPos=array([], shape=(0, 3), dtype=float64), nbRef=array([4], dtype=int32), indices=[], weight=[], showFromIndex=0, showWeights=0, **kwargs):
    """skin a model from a set of rigid dofs


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

		 initPos: initial child coordinates in the world reference frame.

		 nbRef: Number of primitives influencing each point.

		 indices: parent indices for each child.

		 weight: influence weights of the Dofs.

		 showFromIndex: Displayed From Index.

		 showWeights: Show influence.


    """
    return attachedTo.createObject("SkinningMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, initPos=initPos, nbRef=nbRef, indices=indices, weight=weight, showFromIndex=showFromIndex, showWeights=showWeights, **kwargs)
