# -*- coding: utf-8 -*-


"""
Component RigidRigidMapping

.. autofunction:: RigidRigidMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RigidRigidMapping(attachedTo , name='RigidRigidMapping', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, mapForces=1, mapConstraints=1, mapMasses=1, mapMatrices=0, applyRestPosition=0, initialPoints=array([], shape=(0, 7), dtype=float64), repartition=array([], dtype=int32), index=0, filename='', axisLength=0.7, indexFromEnd=0, globalToLocalCoords=0, **kwargs):
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

		 initialPoints: Initial position of the points

		 repartition: number of child frames per parent frame. 
If empty, all the children are attached to the parent with index 
given in the "index" attribute. If one value, each parent frame drives 
the given number of children frames. Otherwise, the values are the number 
of child frames driven by each parent frame. 

		 index: input frame index

		 filename: Xsp file where to load rigidrigid mapping description

		 axisLength: axis length for display

		 indexFromEnd: input DOF index starts from the end of input DOFs vector

		 globalToLocalCoords: are the output DOFs initially expressed in global coordinates


    """
    return attachedTo.createObject("RigidRigidMapping" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, mapForces=mapForces, mapConstraints=mapConstraints, mapMasses=mapMasses, mapMatrices=mapMatrices, applyRestPosition=applyRestPosition, initialPoints=initialPoints, repartition=repartition, index=index, filename=filename, axisLength=axisLength, indexFromEnd=indexFromEnd, globalToLocalCoords=globalToLocalCoords, **kwargs)
