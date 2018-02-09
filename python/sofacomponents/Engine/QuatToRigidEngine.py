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

        
def QuatToRigidEngine(attachedTo , name='QuatToRigidEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, positions=[], orientations=[], colinearPositions=[], rigids=[], **kwargs):
    """Transform a vector of Rigids into two independant vectors for positions (Vec3) and orientations (Quat).


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 positions: Positions (Vector of 3)

		 orientations: Orientations (Quaternion)

		 colinearPositions: Optional positions to restrict output to be colinear in the quaternion Z direction

		 rigids: Rigid (Position + Orientation)


    """
    return attachedTo.createObject("QuatToRigidEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, positions=positions, orientations=orientations, colinearPositions=colinearPositions, rigids=rigids, **kwargs)
