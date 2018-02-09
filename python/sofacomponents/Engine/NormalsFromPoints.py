# -*- coding: utf-8 -*-


"""
Component NormalsFromPoints

.. autofunction:: NormalsFromPoints

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def NormalsFromPoints(attachedTo , name='NormalsFromPoints', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[], triangles=[], quads=[], normals=[], invertNormals=0, useAngles=0, **kwargs):
    """Compute vertex normals by averaging face normals


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: Vertices of the mesh

		 triangles: Triangles of the mesh

		 quads: Quads of the mesh

		 normals: Computed vertex normals of the mesh

		 invertNormals: Swap normals

		 useAngles: Use incident angles to weight faces normal contributions at each vertex


    """
    return attachedTo.createObject("NormalsFromPoints" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, triangles=triangles, quads=quads, normals=normals, invertNormals=invertNormals, useAngles=useAngles, **kwargs)
