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

        
def OglCylinderModel(attachedTo , name='OglCylinderModel', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), restPosition=array([], shape=(0, 3), dtype=float64), normal=array([], shape=(0, 3), dtype=float64), radius=1.0, color=array([1., 1., 1., 1.], dtype=float32), edges=array([], shape=(0, 2), dtype=int32), **kwargs):
    """A simple visualization for set of cylinder.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: Vertices coordinates

		 restPosition: Vertices rest coordinates

		 normal: Normals of the model

		 radius: Radius of the cylinder.

		 color: Color of the cylinders.

		 edges: List of edge indices


    """
    return attachedTo.createObject("OglCylinderModel" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, restPosition=restPosition, normal=normal, radius=radius, color=color, edges=edges, **kwargs)
