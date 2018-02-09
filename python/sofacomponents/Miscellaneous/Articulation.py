# -*- coding: utf-8 -*-


"""
Component Articulation

.. autofunction:: Articulation

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Articulation(attachedTo , name='Articulation', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, axis=[[1.0, 0.0, 0.0]], rotation=0, translation=0, articulationIndex=0, **kwargs):
    """This class defines an articulation by an axis, an orientation and an index.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 axis: Set the rotation axis for the articulation

		 rotation: Rotation

		 translation: Translation

		 articulationIndex: Articulation index


    """
    return attachedTo.createObject("Articulation" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, axis=axis, rotation=rotation, translation=translation, articulationIndex=articulationIndex, **kwargs)
