# -*- coding: utf-8 -*-


"""
Component GenerateGrid

.. autofunction:: GenerateGrid

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GenerateGrid(attachedTo , name='GenerateGrid', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, output_position=[], tetrahedra=[], quads=[], triangles=[], hexahedra=[], min=[[0.0, 0.0, 0.0]], max=[[0.0, 0.0, 0.0]], resolution=[[3, 3, 3]], **kwargs):
    """Generate a Grid Tetrahedral or Hexahedral Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 output_position: output array of 3d points

		 tetrahedra: output mesh tetrahedra

		 quads: output mesh quads

		 triangles: output mesh triangles

		 hexahedra: output mesh hexahedra

		 min: the 3 coordinates of the minimum corner

		 max: the 3 coordinates of the maximum corner

		 resolution: the number of cubes in the x,y,z directions. If resolution in the z direction is  0 then a 2D grid is generated


    """
    return attachedTo.createObject("GenerateGrid" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, output_position=output_position, tetrahedra=tetrahedra, quads=quads, triangles=triangles, hexahedra=hexahedra, min=min, max=max, resolution=resolution, **kwargs)
