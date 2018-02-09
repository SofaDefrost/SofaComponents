# -*- coding: utf-8 -*-


"""
Component VTKExporter

.. autofunction:: VTKExporter

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VTKExporter(attachedTo , name='VTKExporter', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, filename='', XMLformat=1, position=[], edges=1, triangles=0, quads=0, tetras=0, hexas=0, pointsDataFields=[], cellsDataFields=[], exportEveryNumberOfSteps=0, exportAtBegin=0, exportAtEnd=0, overwrite=0, **kwargs):
    """Save State vectors from file at each timestep


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 filename: output VTK file name

		 XMLformat: Set to true to use XML format

		 position: points position (will use points from topology or mechanical state if this is empty)

		 edges: write edge topology

		 triangles: write triangle topology

		 quads: write quad topology

		 tetras: write tetra topology

		 hexas: write hexa topology

		 pointsDataFields: Data to visualize (on points)

		 cellsDataFields: Data to visualize (on cells)

		 exportEveryNumberOfSteps: export file only at specified number of steps (0=disable)

		 exportAtBegin: export file at the initialization

		 exportAtEnd: export file when the simulation is finished

		 overwrite: overwrite the file, otherwise create a new file at each export, with suffix in the filename


    """
    return attachedTo.createObject("VTKExporter" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, XMLformat=XMLformat, position=position, edges=edges, triangles=triangles, quads=quads, tetras=tetras, hexas=hexas, pointsDataFields=pointsDataFields, cellsDataFields=cellsDataFields, exportEveryNumberOfSteps=exportEveryNumberOfSteps, exportAtBegin=exportAtBegin, exportAtEnd=exportAtEnd, overwrite=overwrite, **kwargs)
