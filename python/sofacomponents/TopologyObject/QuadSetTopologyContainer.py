# -*- coding: utf-8 -*-


"""
Component QuadSetTopologyContainer

.. autofunction:: QuadSetTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def QuadSetTopologyContainer(attachedTo , name='QuadSetTopologyContainer', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, fileTopology='', position=[], nbPoints=0, points=[], edges=[], checkConnexity=0, quads=[], **kwargs):
    """Quad set topology container


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

		 edges: List of edge indices

		 checkConnexity: It true, will check the connexity of the mesh.

		 quads: List of quad indices


    """
    return attachedTo.createObject("QuadSetTopologyContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, fileTopology=fileTopology, position=position, nbPoints=nbPoints, points=points, edges=edges, checkConnexity=checkConnexity, quads=quads, **kwargs)
