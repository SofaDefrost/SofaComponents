# -*- coding: utf-8 -*-


"""
Component DisplacementTransformEngine

.. autofunction:: DisplacementTransformEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DisplacementTransformEngine(attachedTo , name='DisplacementTransformEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, x0=array([], shape=(0, 7), dtype=float64), x=array([], shape=(0, 7), dtype=float64), displacements=array([], shape=(0, 7), dtype=float64), **kwargs):
    """Converts a vector of Rigid to a vector of displacement transforms.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 x0: Rest position

		 x: Current position

		 displacements: Displacement transforms with respect to original rigid positions


    """
    return attachedTo.createObject("DisplacementTransformEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, x0=x0, x=x, displacements=displacements, **kwargs)
