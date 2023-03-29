# -*- coding: utf-8 -*-


"""
Component BeamLinearMapping

.. autofunction:: BeamLinearMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BeamLinearMapping(attachedTo , name='BeamLinearMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, localCoord=1, **kwargs):
    """Set the positions and velocities of points attached to a beam using linear interpolation between DOFs


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

		 localCoord: true if initial coordinates are in the beam local coordinate system (i.e. a point at (10,0,0) is on the DOF number 10, whereas if this is false it is at whatever position on the beam where the distance from the initial DOF is 10)


    """
    return attachedTo.createObject("BeamLinearMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, localCoord=localCoord, **kwargs)
