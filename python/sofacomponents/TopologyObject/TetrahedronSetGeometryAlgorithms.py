# -*- coding: utf-8 -*-


"""
Component TetrahedronSetGeometryAlgorithms

.. autofunction:: TetrahedronSetGeometryAlgorithms

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedronSetGeometryAlgorithms(attachedTo , name='TetrahedronSetGeometryAlgorithms', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, showIndicesScale=0.019999999552965164, showPointIndices=0, tagMechanics='', showEdgeIndices=0, drawEdges=0, drawColorEdges='0.4 1 0.3 1', showTriangleIndices=0, drawTriangles=0, drawColorTriangles=[[0.20000000298023224, 1.0, 1.0, 1.0]], drawNormals=0, drawNormalLength=10.0, recomputeTrianglesOrientation=0, flipNormals=0, showTetrahedraIndices=0, drawTetrahedra=0, drawScaleTetrahedra=1.0, drawColorTetrahedra=[[1.0, 1.0, 0.0, 1.0]], **kwargs):
    """Tetrahedron set geometry algorithms


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

		 showTriangleIndices: Debug : view Triangle indices

		 drawTriangles: if true, draw the triangles in the topology

		 drawColorTriangles: RGBA code color used to draw edges.

		 drawNormals: if true, draw the triangles in the topology

		 drawNormalLength: Fiber length visualisation.

		 recomputeTrianglesOrientation: if true, will recompute triangles orientation according to normals.

		 flipNormals: if true, will flip normal of the first triangle used to recompute triangle orientation.

		 showTetrahedraIndices: Debug : view Tetrahedrons indices

		 drawTetrahedra: if true, draw the tetrahedra in the topology

		 drawScaleTetrahedra: Scale of the terahedra (between 0 and 1; if <1.0, it produces gaps between the tetrahedra)

		 drawColorTetrahedra: RGBA code color used to draw tetrahedra.


    """
    return attachedTo.createObject("TetrahedronSetGeometryAlgorithms" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, showIndicesScale=showIndicesScale, showPointIndices=showPointIndices, tagMechanics=tagMechanics, showEdgeIndices=showEdgeIndices, drawEdges=drawEdges, drawColorEdges=drawColorEdges, showTriangleIndices=showTriangleIndices, drawTriangles=drawTriangles, drawColorTriangles=drawColorTriangles, drawNormals=drawNormals, drawNormalLength=drawNormalLength, recomputeTrianglesOrientation=recomputeTrianglesOrientation, flipNormals=flipNormals, showTetrahedraIndices=showTetrahedraIndices, drawTetrahedra=drawTetrahedra, drawScaleTetrahedra=drawScaleTetrahedra, drawColorTetrahedra=drawColorTetrahedra, **kwargs)
