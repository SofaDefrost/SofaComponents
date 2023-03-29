# -*- coding: utf-8 -*-


"""
Component Vertex2Frame

.. autofunction:: Vertex2Frame

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Vertex2Frame(attachedTo , name='Vertex2Frame', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), texCoords=array([], shape=(0, 2), dtype=float64), normals=array([], shape=(0, 3), dtype=float64), frames=array([], shape=(0, 7), dtype=float64), useNormals=1, invertNormals=0, rotation=0, rotationAngle=0.0, **kwargs):
    """

    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: Vertices of the mesh loaded

		 texCoords: TexCoords of the mesh loaded

		 normals: Normals of the mesh loaded

		 frames: Frames at output

		 useNormals: Use normals to compute the orientations; if disabled the direction of the x axisof a vertice is the one from this vertice to the next one

		 invertNormals: Swap normals

		 rotation: Apply a local rotation on the frames. If 0 a x-axis rotation is applied. If 1 a y-axis rotation is applied, If 2 a z-axis rotation is applied.

		 rotationAngle: Angle rotation


    """
    return attachedTo.createObject("Vertex2Frame" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, texCoords=texCoords, normals=normals, frames=frames, useNormals=useNormals, invertNormals=invertNormals, rotation=rotation, rotationAngle=rotationAngle, **kwargs)
