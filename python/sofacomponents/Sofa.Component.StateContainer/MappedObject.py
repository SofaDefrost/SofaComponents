# -*- coding: utf-8 -*-


"""
Component MappedObject

.. autofunction:: MappedObject

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MappedObject(attachedTo , name='MappedObject', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), velocity=array([], shape=(0, 3), dtype=float64), **kwargs):
    """Mapped state vectors


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: position vector

		 velocity: velocity vector


    """
    return attachedTo.createObject("MappedObject" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, velocity=velocity, **kwargs)
