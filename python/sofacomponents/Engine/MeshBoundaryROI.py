# -*- coding: utf-8 -*-


"""
Component MeshBoundaryROI

.. autofunction:: MeshBoundaryROI

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshBoundaryROI(attachedTo , name='MeshBoundaryROI', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, triangles=[], quads=[], inputROI=[], indices=[], **kwargs):
    """Outputs indices of boundary vertices of a triangle/quad mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 triangles: input triangles

		 quads: input quads

		 inputROI: optional subset of the input mesh

		 indices: Index lists of the closing vertices


    """
    return attachedTo.createObject("MeshBoundaryROI" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, triangles=triangles, quads=quads, inputROI=inputROI, indices=indices, **kwargs)
