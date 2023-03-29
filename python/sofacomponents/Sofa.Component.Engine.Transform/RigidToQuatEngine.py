# -*- coding: utf-8 -*-


"""
Component RigidToQuatEngine

.. autofunction:: RigidToQuatEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RigidToQuatEngine(attachedTo , name='RigidToQuatEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, positions=array([], shape=(0, 3), dtype=float64), orientations=array([], shape=(0, 4), dtype=float64), orientationsEuler=array([], shape=(0, 3), dtype=float64), rigids=array([], shape=(0, 7), dtype=float64), **kwargs):
    """Transform a couple of Vec3 and Quaternion in Rigid


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 positions: Positions (Vector of 3)

		 orientations: Orientations (Quaternion)

		 orientationsEuler: Orientations (Euler angle)

		 rigids: Rigid (Position + Orientation)


    """
    return attachedTo.createObject("RigidToQuatEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, positions=positions, orientations=orientations, orientationsEuler=orientationsEuler, rigids=rigids, **kwargs)
