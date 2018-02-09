# -*- coding: utf-8 -*-


"""
Component ValuesFromPositions

.. autofunction:: ValuesFromPositions

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ValuesFromPositions(attachedTo , name='ValuesFromPositions', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inputValues=[], direction=[[0.0, 1.0, 0.0]], position=[], edges=[], triangles=[], tetrahedra=[], values=[], edgeValues=[], triangleValues=[], tetrahedronValues=[], pointVectors=[], edgeVectors=[], triangleVectors=[], tetrahedronVectors=[], fieldType='Scalar', drawVectors=0, drawVectorLength=10.0, **kwargs):
    """Assign values to primitives (vertex/edge/triangle/tetrahedron) based on a linear interpolation of values along a direction


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inputValues: Input values

		 direction: Direction along which the values are interpolated

		 position: Rest position coordinates of the degrees of freedom

		 edges: Edge Topology

		 triangles: Triangle Topology

		 tetrahedra: Tetrahedron Topology

		 values: Values of the points contained in the ROI

		 edgeValues: Values of the edges contained in the ROI

		 triangleValues: Values of the triangles contained in the ROI

		 tetrahedronValues: Values of the tetrahedra contained in the ROI

		 pointVectors: Vectors of the points contained in the ROI

		 edgeVectors: Vectors of the edges contained in the ROI

		 triangleVectors: Vectors of the triangles contained in the ROI

		 tetrahedronVectors: Vectors of the tetrahedra contained in the ROI

		 fieldType: field type of output elements

		 drawVectors: draw vectors line

		 drawVectorLength: vector length visualisation. 


    """
    return attachedTo.createObject("ValuesFromPositions" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inputValues=inputValues, direction=direction, position=position, edges=edges, triangles=triangles, tetrahedra=tetrahedra, values=values, edgeValues=edgeValues, triangleValues=triangleValues, tetrahedronValues=tetrahedronValues, pointVectors=pointVectors, edgeVectors=edgeVectors, triangleVectors=triangleVectors, tetrahedronVectors=tetrahedronVectors, fieldType=fieldType, drawVectors=drawVectors, drawVectorLength=drawVectorLength, **kwargs)
