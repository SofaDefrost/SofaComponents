# -*- coding: utf-8 -*-


"""
Component TubularMapping

.. autofunction:: TubularMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TubularMapping(attachedTo , name='TubularMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, nbPointsOnEachCircle=0, radius=0.0, peak=0, **kwargs):
    """Create a Tube around rigid points


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

		 nbPointsOnEachCircle: Discretization of created circles

		 radius: Radius of created circles

		 peak: =0 no peak, =1 peak on the first segment =2 peak on the two first segment, =-1 peak on the last segment


    """
    return attachedTo.createObject("TubularMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, nbPointsOnEachCircle=nbPointsOnEachCircle, radius=radius, peak=peak, **kwargs)
