# -*- coding: utf-8 -*-


"""
Component PointSetTopologyContainer

.. autofunction:: PointSetTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PointSetTopologyContainer(attachedTo , name='PointSetTopologyContainer', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, fileTopology='', position=[], nbPoints=0, points=[], **kwargs):
    """Point set topology container


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 fileTopology: Filename of the mesh

		 position: Initial position of points

		 nbPoints: Number of points

		 points: List of point indices


    """
    return attachedTo.createObject("PointSetTopologyContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, fileTopology=fileTopology, position=position, nbPoints=nbPoints, points=points, **kwargs)
