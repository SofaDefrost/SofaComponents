# -*- coding: utf-8 -*-


"""
Component TriangularConvexHull3D

.. autofunction:: TriangularConvexHull3D

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangularConvexHull3D(attachedTo , name='TriangularConvexHull3D', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inputPoints=[], outputPoints=[], outputTriangles=[], **kwargs):
    """Generate triangular convex hull around points


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inputPoints: Rest position coordinates of the degrees of freedom

		 outputPoints: New Rest position coordinates

		 outputTriangles: List of triangles


    """
    return attachedTo.createObject("TriangularConvexHull3D" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inputPoints=inputPoints, outputPoints=outputPoints, outputTriangles=outputTriangles, **kwargs)
