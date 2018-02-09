# -*- coding: utf-8 -*-


"""
Component QuadSetGeometryAlgorithms

.. autofunction:: QuadSetGeometryAlgorithms

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def QuadSetGeometryAlgorithms(attachedTo , name='QuadSetGeometryAlgorithms', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, showIndicesScale=0.019999999552965164, showPointIndices=0, tagMechanics='', showEdgeIndices=0, drawEdges=0, drawColorEdges='0.4 1 0.3 1', showQuadIndices=0, drawQuads=0, drawColorQuads=[[0.0, 0.4000000059604645, 0.4000000059604645]], **kwargs):
    """Quad set geometry algorithms


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 showIndicesScale: Debug : scale for view topology indices

		 showPointIndices: Debug : view Point indices

		 tagMechanics: Tag of the Mechanical Object

		 showEdgeIndices: Debug : view Edge indices.

		 drawEdges: if true, draw the edges in the topology.

		 drawColorEdges: RGB code color used to draw edges.

		 showQuadIndices: Debug : view Quad indices

		 drawQuads: if true, draw the quads in the topology

		 drawColorQuads: RGB code color used to draw quads.


    """
    return attachedTo.createObject("QuadSetGeometryAlgorithms" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, showIndicesScale=showIndicesScale, showPointIndices=showPointIndices, tagMechanics=tagMechanics, showEdgeIndices=showEdgeIndices, drawEdges=drawEdges, drawColorEdges=drawColorEdges, showQuadIndices=showQuadIndices, drawQuads=drawQuads, drawColorQuads=drawColorQuads, **kwargs)
