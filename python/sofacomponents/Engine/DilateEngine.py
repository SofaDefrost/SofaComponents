# -*- coding: utf-8 -*-


"""
Component DilateEngine

.. autofunction:: DilateEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DilateEngine(attachedTo , name='DilateEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, input_position=[], output_position=[], triangles=[], quads=[], normal=[], thickness=[], distance=0.0, minThickness=0.0, **kwargs):
    """Dilates a given mesh by moving vertices along their normal.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 input_position: input array of 3d points

		 output_position: output array of 3d points

		 triangles: input mesh triangles

		 quads: input mesh quads

		 normal: point normals

		 thickness: point thickness

		 distance: distance to move the points (positive for dilatation, negative for erosion)

		 minThickness: minimal thickness to enforce


    """
    return attachedTo.createObject("DilateEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, input_position=input_position, output_position=output_position, triangles=triangles, quads=quads, normal=normal, thickness=thickness, distance=distance, minThickness=minThickness, **kwargs)
