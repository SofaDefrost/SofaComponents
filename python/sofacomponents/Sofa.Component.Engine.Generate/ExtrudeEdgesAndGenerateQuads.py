# -*- coding: utf-8 -*-


"""
Component ExtrudeEdgesAndGenerateQuads

.. autofunction:: ExtrudeEdgesAndGenerateQuads

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ExtrudeEdgesAndGenerateQuads(attachedTo , name='ExtrudeEdgesAndGenerateQuads', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, extrudeDirection=array([1., 0., 0.]), thicknessIn=0.0, thicknessOut=1.0, numberOfSections=1, curveVertices=array([], shape=(0, 3), dtype=float64), curveEdges=array([], shape=(0, 2), dtype=int32), extrudedVertices=array([], shape=(0, 3), dtype=float64), extrudedEdges=array([], shape=(0, 2), dtype=int32), extrudedQuads=array([], shape=(0, 4), dtype=int32), **kwargs):
    """This engine extrudes an edge-based curve into a quad surface patch


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 extrudeDirection: Direction along which to extrude the curve

		 thicknessIn: Thickness of the extruded volume in the opposite direction of the normals

		 thicknessOut: Thickness of the extruded volume in the direction of the normals

		 numberOfSections: Number of sections / steps in the extrusion

		 curveVertices: Position coordinates along the initial curve

		 curveEdges: Indices of the edges of the curve to extrude

		 extrudedVertices: Coordinates of the extruded vertices

		 extrudedEdges: List of all edges generated during the extrusion

		 extrudedQuads: List of all quads generated during the extrusion


    """
    return attachedTo.createObject("ExtrudeEdgesAndGenerateQuads" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, extrudeDirection=extrudeDirection, thicknessIn=thicknessIn, thicknessOut=thicknessOut, numberOfSections=numberOfSections, curveVertices=curveVertices, curveEdges=curveEdges, extrudedVertices=extrudedVertices, extrudedEdges=extrudedEdges, extrudedQuads=extrudedQuads, **kwargs)
