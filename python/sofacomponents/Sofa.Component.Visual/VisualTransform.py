# -*- coding: utf-8 -*-


"""
Component VisualTransform

.. autofunction:: VisualTransform

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VisualTransform(attachedTo , name='VisualTransform', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, transform=array([0., 0., 0., 0., 0., 0., 1.]), recursive=0, **kwargs):
    """TODO


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 transform: Transformation to apply

		 recursive: True to apply transform to all nodes below


    """
    return attachedTo.createObject("VisualTransform" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, transform=transform, recursive=recursive, **kwargs)
