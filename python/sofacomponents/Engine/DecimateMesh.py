# -*- coding: utf-8 -*-


"""
Component DecimateMesh

.. autofunction:: DecimateMesh

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DecimateMesh(attachedTo , name='DecimateMesh', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inputVertices=[], inputTriangles=[], targetedNumberOfEdges=0, targetedRatioOfEdges=0.0, outputPoints=[], outputTriangles=[], outputNormals=[], writeToFile=0, **kwargs):
    """Simplification of a mesh by the process of reducing the number of faces


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inputVertices: List of vertices

		 inputTriangles: List of triangles

		 targetedNumberOfEdges: Desired number of edges after simplification

		 targetedRatioOfEdges: Ratio between the number of edges and number of initial edges

		 outputPoints: New vertices after decimation

		 outputTriangles: New triangles after decimation

		 outputNormals: New normals after decimation

		 writeToFile: Writes the decimated mesh into a file


    """
    return attachedTo.createObject("DecimateMesh" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inputVertices=inputVertices, inputTriangles=inputTriangles, targetedNumberOfEdges=targetedNumberOfEdges, targetedRatioOfEdges=targetedRatioOfEdges, outputPoints=outputPoints, outputTriangles=outputTriangles, outputNormals=outputNormals, writeToFile=writeToFile, **kwargs)
