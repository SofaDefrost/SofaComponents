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

        
def MappedObject(attachedTo , name='MappedObject', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[], velocity=[], **kwargs):
    """Mapped state vectors


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: position vector

		 velocity: velocity vector


    """
    return attachedTo.createObject("MappedObject" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, velocity=velocity, **kwargs)
