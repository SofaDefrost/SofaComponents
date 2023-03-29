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

        
def ExtrudeSurface(attachedTo , name='ExtrudeSurface', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isVisible=1, heightFactor=1.0, triangles=array([], shape=(0, 3), dtype=int32), extrusionVertices=array([], shape=(0, 3), dtype=float64), surfaceVertices=array([], shape=(0, 3), dtype=float64), extrusionTriangles=array([], shape=(0, 3), dtype=int32), surfaceTriangles=array([], dtype=int32), **kwargs):
    """This class truns on spiral any topological model


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isVisible: is Visible ?

		 heightFactor: Factor for the height of the extrusion (based on normal) ?

		 triangles: List of triangle indices

		 extrusionVertices: Position coordinates of the extrusion

		 surfaceVertices: Position coordinates of the surface

		 extrusionTriangles: Triangles indices of the extrusion

		 surfaceTriangles: Indices of the triangles of the surface to extrude


    """
    return attachedTo.createObject("ExtrudeSurface" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isVisible=isVisible, heightFactor=heightFactor, triangles=triangles, extrusionVertices=extrusionVertices, surfaceVertices=surfaceVertices, extrusionTriangles=extrusionTriangles, surfaceTriangles=surfaceTriangles, **kwargs)
