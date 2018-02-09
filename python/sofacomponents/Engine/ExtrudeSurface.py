# -*- coding: utf-8 -*-


"""
Component ExtrudeSurface

.. autofunction:: ExtrudeSurface

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ExtrudeSurface(attachedTo , name='ExtrudeSurface', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isVisible=1, heightFactor=1.0, triangles=[], extrusionVertices=[], surfaceVertices=[], extrusionTriangles=[], surfaceTriangles=[], **kwargs):
    """This class truns on spiral any topological model


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isVisible: is Visible ?

		 heightFactor: Factor for the height of the extrusion (based on normal) ?

		 triangles: List of triangle indices

		 extrusionVertices: Position coordinates of the extrusion

		 surfaceVertices: Position coordinates of the surface

		 extrusionTriangles: Triangles indices of the extrusion

		 surfaceTriangles: Indices of the triangles of the surface to extrude


    """
    return attachedTo.createObject("ExtrudeSurface" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isVisible=isVisible, heightFactor=heightFactor, triangles=triangles, extrusionVertices=extrusionVertices, surfaceVertices=surfaceVertices, extrusionTriangles=extrusionTriangles, surfaceTriangles=surfaceTriangles, **kwargs)
