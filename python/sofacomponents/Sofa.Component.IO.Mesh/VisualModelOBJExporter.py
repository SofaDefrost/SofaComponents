# -*- coding: utf-8 -*-


"""
Component VisualModelOBJExporter

.. autofunction:: VisualModelOBJExporter

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VisualModelOBJExporter(attachedTo , name='VisualModelOBJExporter', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, filename='', exportEveryNumberOfSteps=0, exportAtBegin=0, exportAtEnd=0, enable=1, **kwargs):
    """Export the scene under the Wavefront OBJ format.When several frames are exported the file name have the following pattern: outfile000.obj outfile001.obj.


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


    """
    return attachedTo.createObject("VisualModelOBJExporter" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, exportEveryNumberOfSteps=exportEveryNumberOfSteps, exportAtBegin=exportAtBegin, exportAtEnd=exportAtEnd, enable=enable, **kwargs)
