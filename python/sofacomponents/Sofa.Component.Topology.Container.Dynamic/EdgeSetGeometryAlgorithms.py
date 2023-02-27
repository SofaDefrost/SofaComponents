# -*- coding: utf-8 -*-


"""
Component EdgeSetGeometryAlgorithms

.. autofunction:: EdgeSetGeometryAlgorithms

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EdgeSetGeometryAlgorithms(attachedTo , name='EdgeSetGeometryAlgorithms', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, showIndicesScale=0.019999999552965164, showPointIndices=0, tagMechanics='', showEdgeIndices=0, drawEdges=0, drawColorEdges=array([0.4, 1. , 0.3, 1. ], dtype=float32), **kwargs):
    """Edge set geometry algorithms


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 showIndicesScale: Debug : scale for view topology indices

		 showPointIndices: Debug : view Point indices

		 tagMechanics: Tag of the Mechanical Object

		 showEdgeIndices: Debug : view Edge indices.

		 drawEdges: if true, draw the edges in the topology.

		 drawColorEdges: RGB code color used to draw edges.


    """
    return attachedTo.createObject("EdgeSetGeometryAlgorithms" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, showIndicesScale=showIndicesScale, showPointIndices=showPointIndices, tagMechanics=tagMechanics, showEdgeIndices=showEdgeIndices, drawEdges=drawEdges, drawColorEdges=drawColorEdges, **kwargs)
