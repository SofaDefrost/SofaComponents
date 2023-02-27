# -*- coding: utf-8 -*-


"""
Component DisplacementMatrixEngine

.. autofunction:: DisplacementMatrixEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DisplacementMatrixEngine(attachedTo , name='DisplacementMatrixEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, x0=array([], shape=(0, 7), dtype=float64), x=array([], shape=(0, 7), dtype=float64), displaceMats=array([], shape=(0, 16), dtype=float64), scales=array([], shape=(0, 3), dtype=float64), **kwargs):
    """Converts a vector of Rigid to a vector of displacement matrices.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 x0: Rest position

		 x: Current position

		 displaceMats: Displacement transforms with respect to original rigid positions

		 scales: Scale transformation added to the rigid transformation


    """
    return attachedTo.createObject("DisplacementMatrixEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, x0=x0, x=x, displaceMats=displaceMats, scales=scales, **kwargs)
