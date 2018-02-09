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

        
def RigidToQuatEngine(attachedTo , name='RigidToQuatEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, positions=[], orientations=[], rigids=[], **kwargs):
    """Transform a couple of Vec3 and Quaternion in Rigid


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 positions: Positions (Vector of 3)

		 orientations: Orientations (Quaternion)

		 rigids: Rigid (Position + Orientation)


    """
    return attachedTo.createObject("RigidToQuatEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, positions=positions, orientations=orientations, rigids=rigids, **kwargs)
