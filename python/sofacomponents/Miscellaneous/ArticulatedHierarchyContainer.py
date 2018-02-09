# -*- coding: utf-8 -*-


"""
Component ArticulatedHierarchyContainer

.. autofunction:: ArticulatedHierarchyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ArticulatedHierarchyContainer(attachedTo , name='ArticulatedHierarchyContainer', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, filename='', **kwargs):
    """This class allow to store and retrieve all the articulation centers from an articulated rigid object


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 filename: BVH File to load the articulation


    """
    return attachedTo.createObject("ArticulatedHierarchyContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, **kwargs)
