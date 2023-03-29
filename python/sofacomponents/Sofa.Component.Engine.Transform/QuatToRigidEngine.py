# -*- coding: utf-8 -*-


"""
Component QuatToRigidEngine

.. autofunction:: QuatToRigidEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def QuatToRigidEngine(attachedTo , name='QuatToRigidEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, positions=array([], shape=(0, 3), dtype=float64), orientations=array([], shape=(0, 4), dtype=float64), colinearPositions=array([], shape=(0, 3), dtype=float64), rigids=array([], shape=(0, 7), dtype=float64), **kwargs):
    """Transform a vector of Rigids into two independant vectors for positions (Vec3) and orientations (Quat).


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 positions: Positions (Vector of 3)

		 orientations: Orientations (Quaternion)

		 colinearPositions: Optional positions to restrict output to be colinear in the quaternion Z direction

		 rigids: Rigid (Position + Orientation)


    """
    return attachedTo.createObject("QuatToRigidEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, positions=positions, orientations=orientations, colinearPositions=colinearPositions, rigids=rigids, **kwargs)
