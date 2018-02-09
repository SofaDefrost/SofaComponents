# -*- coding: utf-8 -*-


"""
Component PointsFromIndices

.. autofunction:: PointsFromIndices

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PointsFromIndices(attachedTo , name='PointsFromIndices', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[], indices=[], indices_position=[], **kwargs):
    """Find the points given a list of indices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: Position coordinates of the degrees of freedom

		 indices: Indices of the points

		 indices_position: Coordinates of the points contained in indices


    """
    return attachedTo.createObject("PointsFromIndices" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, indices=indices, indices_position=indices_position, **kwargs)
