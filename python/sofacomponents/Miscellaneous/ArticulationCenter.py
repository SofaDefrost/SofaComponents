# -*- coding: utf-8 -*-


"""
Component ArticulationCenter

.. autofunction:: ArticulationCenter

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ArticulationCenter(attachedTo , name='ArticulationCenter', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, parentIndex=0, childIndex=0, globalPosition=[[0.0, 0.0, 0.0]], posOnParent=[[0.0, 0.0, 0.0]], posOnChild=[[0.0, 0.0, 0.0]], articulationProcess=0, **kwargs):
    """This class defines an articulation center. This contains a set of articulations.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 parentIndex: Parent of the center articulation

		 childIndex: Child of the center articulation

		 globalPosition: Global position of the articulation center

		 posOnParent: Parent position of the articulation center

		 posOnChild: Child position of the articulation center

		 articulationProcess:  0 - (default) hierarchy between articulations (euler angles)
 1- ( on Parent) no hierarchy - axis are attached to the parent
 2- (attached on Child) no hierarchy - axis are attached to the child


    """
    return attachedTo.createObject("ArticulationCenter" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, parentIndex=parentIndex, childIndex=childIndex, globalPosition=globalPosition, posOnParent=posOnParent, posOnChild=posOnChild, articulationProcess=articulationProcess, **kwargs)
