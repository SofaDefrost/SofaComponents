# -*- coding: utf-8 -*-


"""
Component TransformEngine

.. autofunction:: TransformEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TransformEngine(attachedTo , name='TransformEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, input_position=array([], shape=(0, 3), dtype=float64), output_position=array([], shape=(0, 3), dtype=float64), translation=array([0., 0., 0.]), rotation=array([0., 0., 0.]), quaternion=array([0., 0., 0., 1.]), scale=array([1., 1., 1.]), inverse=0, **kwargs):
    """Transform position of 3d points


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 input_position: input array of 3d points

		 output_position: output array of 3d points

		 translation: translation vector 

		 rotation: rotation vector 

		 quaternion: rotation quaternion 

		 scale: scale factor

		 inverse: true to apply inverse transformation


    """
    return attachedTo.createObject("TransformEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, input_position=input_position, output_position=output_position, translation=translation, rotation=rotation, quaternion=quaternion, scale=scale, inverse=inverse, **kwargs)
