# -*- coding: utf-8 -*-


"""
Component VisualGrid

.. autofunction:: VisualGrid

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VisualGrid(attachedTo , name='VisualGrid', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Loading', listening=0, plane='z', size=10.0, nbSubdiv=16, color=array([0.34117648, 0.34117648, 0.34117648, 1.        ], dtype=float32), thickness=1.0, draw=1, **kwargs):
    """Display a simple grid


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 plane: Plane of the grid

		 size: Size of the squared grid

		 nbSubdiv: Number of subdivisions

		 color: Color of the lines in the grid. default=(0.34,0.34,0.34,1.0)

		 thickness: Thickness of the lines in the grid

		 draw: Display the grid or not


    """
    return attachedTo.createObject("VisualGrid" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, plane=plane, size=size, nbSubdiv=nbSubdiv, color=color, thickness=thickness, draw=draw, **kwargs)
