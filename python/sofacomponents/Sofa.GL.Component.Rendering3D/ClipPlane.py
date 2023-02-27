# -*- coding: utf-8 -*-


"""
Component ClipPlane

.. autofunction:: ClipPlane

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ClipPlane(attachedTo , name='ClipPlane', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([0., 0., 0.]), normal=array([1., 0., 0.]), id=0, active=1, **kwargs):
    """OpenGL Clipping Plane


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: Point crossed by the clipping plane

		 normal: Normal of the clipping plane, pointing toward the clipped region

		 id: Clipping plane OpenGL ID

		 active: Control whether the clipping plane should be applied or not


    """
    return attachedTo.createObject("ClipPlane" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, normal=normal, id=id, active=active, **kwargs)
