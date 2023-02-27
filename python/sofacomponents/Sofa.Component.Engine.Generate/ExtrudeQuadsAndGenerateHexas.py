# -*- coding: utf-8 -*-


"""
Component ExtrudeQuadsAndGenerateHexas

.. autofunction:: ExtrudeQuadsAndGenerateHexas

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ExtrudeQuadsAndGenerateHexas(attachedTo , name='ExtrudeQuadsAndGenerateHexas', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isVisible=1, scale=array([1., 1., 1.]), thicknessIn=0.0, thicknessOut=1.0, numberOfSlices=1, flipNormals=0, surfaceVertices=array([], shape=(0, 3), dtype=float64), surfaceQuads=array([], shape=(0, 4), dtype=int32), extrudedVertices=array([], shape=(0, 3), dtype=float64), extrudedSurfaceQuads=array([], shape=(0, 4), dtype=int32), extrudedQuads=array([], shape=(0, 4), dtype=int32), extrudedHexas=array([], shape=(0, 8), dtype=int32), **kwargs):
    """This engine extrudes a quad-based surface into a set of hexahedral elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isVisible: is Visible ?

		 scale: Apply a scaling factor to the extruded mesh

		 thicknessIn: Thickness of the extruded volume in the opposite direction of the normals

		 thicknessOut: Thickness of the extruded volume in the direction of the normals

		 numberOfSlices: Number of slices / steps in the extrusion

		 flipNormals: If true, will inverse point order when creating hexa

		 surfaceVertices: Position coordinates of the surface

		 surfaceQuads: Indices of the quads of the surface to extrude

		 extrudedVertices: Coordinates of the extruded vertices

		 extrudedSurfaceQuads: List of new surface quads generated during the extrusion

		 extrudedQuads: List of all quads generated during the extrusion

		 extrudedHexas: List of hexahedra generated during the extrusion


    """
    return attachedTo.createObject("ExtrudeQuadsAndGenerateHexas" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isVisible=isVisible, scale=scale, thicknessIn=thicknessIn, thicknessOut=thicknessOut, numberOfSlices=numberOfSlices, flipNormals=flipNormals, surfaceVertices=surfaceVertices, surfaceQuads=surfaceQuads, extrudedVertices=extrudedVertices, extrudedSurfaceQuads=extrudedSurfaceQuads, extrudedQuads=extrudedQuads, extrudedHexas=extrudedHexas, **kwargs)
