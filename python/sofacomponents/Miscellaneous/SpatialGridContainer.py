# -*- coding: utf-8 -*-


"""
Component SpatialGridContainer

.. autofunction:: SpatialGridContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SpatialGridContainer(attachedTo , name='SpatialGridContainer', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, cellWidth=1.0, showGrid=0, autoUpdate=0, sortPoints=0, **kwargs):
    """Hashing spatial grid container, used for SPH fluids for instance.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 cellWidth: Width each cell in the grid. If it is used to compute neighboors, it should be greater that the max radius considered.

		 showGrid: activate rendering of the grid

		 autoUpdate: Automatically update the grid at each iteration.

		 sortPoints: Sort points depending on which cell they are in the grid. This is required for efficient collision detection.


    """
    return attachedTo.createObject("SpatialGridContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, cellWidth=cellWidth, showGrid=showGrid, autoUpdate=autoUpdate, sortPoints=sortPoints, **kwargs)
