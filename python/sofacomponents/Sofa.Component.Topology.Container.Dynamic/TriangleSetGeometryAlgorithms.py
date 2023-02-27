# -*- coding: utf-8 -*-


"""
Component TriangleSetGeometryAlgorithms

.. autofunction:: TriangleSetGeometryAlgorithms

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangleSetGeometryAlgorithms(attachedTo , name='TriangleSetGeometryAlgorithms', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, showIndicesScale=0.019999999552965164, showPointIndices=0, tagMechanics='', showEdgeIndices=0, drawEdges=0, drawColorEdges=array([0.4, 1. , 0.3, 1. ], dtype=float32), showTriangleIndices=0, drawTriangles=0, drawColorTriangles=array([0.3, 0.5, 0.8, 1. ], dtype=float32), drawNormals=0, drawNormalLength=10.0, recomputeTrianglesOrientation=0, flipNormals=0, **kwargs):
    """Triangle set geometry algorithms


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

		 showTriangleIndices: Debug : view Triangle indices

		 drawTriangles: if true, draw the triangles in the topology

		 drawColorTriangles: RGBA code color used to draw edges.

		 drawNormals: if true, draw the triangles in the topology

		 drawNormalLength: Fiber length visualisation.

		 recomputeTrianglesOrientation: if true, will recompute triangles orientation according to normals.

		 flipNormals: if true, will flip normal of the first triangle used to recompute triangle orientation.


    """
    return attachedTo.createObject("TriangleSetGeometryAlgorithms" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, showIndicesScale=showIndicesScale, showPointIndices=showPointIndices, tagMechanics=tagMechanics, showEdgeIndices=showEdgeIndices, drawEdges=drawEdges, drawColorEdges=drawColorEdges, showTriangleIndices=showTriangleIndices, drawTriangles=drawTriangles, drawColorTriangles=drawColorTriangles, drawNormals=drawNormals, drawNormalLength=drawNormalLength, recomputeTrianglesOrientation=recomputeTrianglesOrientation, flipNormals=flipNormals, **kwargs)
