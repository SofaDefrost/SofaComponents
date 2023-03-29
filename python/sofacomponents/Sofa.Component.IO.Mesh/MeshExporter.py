# -*- coding: utf-8 -*-


"""
Component MeshExporter

.. autofunction:: MeshExporter

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshExporter(attachedTo , name='MeshExporter', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, filename='', exportEveryNumberOfSteps=0, exportAtBegin=0, exportAtEnd=0, enable=1, format='ALL', position=array([], shape=(0, 3), dtype=float64), edges=1, triangles=1, quads=1, tetras=1, hexas=1, **kwargs):
    """Export topology and positions into file.   
Supported format are:   
- vtkxml  
- vtk  
- netgen  
- teten  
- gmsh  
- obj  



    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 filename: Path or filename where to export the data.  If missing the name of the component is used.

		 exportEveryNumberOfSteps: export file only at specified number of steps (0=disable, default=0)

		 exportAtBegin: export file at the initialization (default=false)

		 exportAtEnd: export file when the simulation is finished (default=false)

		 enable: Enable or disable the component. (default=true)

		 format: File format to use

		 position: points position (will use points from topology or mechanical state if this is empty)

		 edges: write edge topology

		 triangles: write triangle topology

		 quads: write quad topology

		 tetras: write tetra topology

		 hexas: write hexa topology


    """
    return attachedTo.createObject("MeshExporter" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, exportEveryNumberOfSteps=exportEveryNumberOfSteps, exportAtBegin=exportAtBegin, exportAtEnd=exportAtEnd, enable=enable, format=format, position=position, edges=edges, triangles=triangles, quads=quads, tetras=tetras, hexas=hexas, **kwargs)
