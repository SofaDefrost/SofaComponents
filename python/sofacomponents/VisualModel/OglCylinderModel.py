# -*- coding: utf-8 -*-


"""
Component OglCylinderModel

.. autofunction:: OglCylinderModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglCylinderModel(attachedTo , name='OglCylinderModel', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[], restPosition=[], normal=[], radius=1.0, color='1 1 1 1', edges=[], **kwargs):
    """A simple visualization for set of cylinder.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: Vertices coordinates

		 restPosition: Vertices rest coordinates

		 normal: Normals of the model

		 radius: Radius of the cylinder.

		 color: Color of the cylinders.

		 edges: List of edge indices


    """
    return attachedTo.createObject("OglCylinderModel" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, restPosition=restPosition, normal=normal, radius=radius, color=color, edges=edges, **kwargs)
