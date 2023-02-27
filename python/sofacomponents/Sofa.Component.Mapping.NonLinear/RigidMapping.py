# -*- coding: utf-8 -*-


"""
Component RigidMapping

.. autofunction:: RigidMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RigidMapping(attachedTo , name='RigidMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, initialPoints=array([], shape=(0, 3), dtype=float64), index=0, filename='', useX0=0, indexFromEnd=0, rigidIndexPerPoint=array([], dtype=int32), globalToLocalCoords=0, geometricStiffness=0, **kwargs):
    """Set the positions and velocities of points attached to a rigid parent


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

		 initialPoints: Local Coordinates of the points

		 index: input DOF index

		 filename: Xsp file where rigid mapping information can be loaded from.

		 useX0: Use x0 instead of local copy of initial positions (to support topo changes)

		 indexFromEnd: input DOF index starts from the end of input DOFs vector

		 rigidIndexPerPoint: For each mapped point, the index of the Rigid it is mapped from

		 globalToLocalCoords: are the output DOFs initially expressed in global coordinates

		 geometricStiffness: assemble (and use) geometric stiffness (0=no GS, 1=non symmetric, 2=symmetrized)


    """
    return attachedTo.createObject("RigidMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, initialPoints=initialPoints, index=index, filename=filename, useX0=useX0, indexFromEnd=indexFromEnd, rigidIndexPerPoint=rigidIndexPerPoint, globalToLocalCoords=globalToLocalCoords, geometricStiffness=geometricStiffness, **kwargs)
