# -*- coding: utf-8 -*-


"""
Component TransformPosition

.. autofunction:: TransformPosition

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TransformPosition(attachedTo , name='TransformPosition', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, origin=array([0., 0., 0.]), input_position=array([], shape=(0, 3), dtype=float64), output_position=array([], shape=(0, 3), dtype=float64), normal=array([0., 0., 0.]), translation=array([0., 0., 0.]), rotation=array([0., 0., 0.]), scale=array([1., 1., 1.]), matrix=array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]]), method='projectOnPlane', seedValue=0, maxRandomDisplacement=1.0, fixedIndices=array([], dtype=int32), filename='', drawInput=0, drawOutput=0, pointSize=1.0, **kwargs):
    """Transform position of 3d points


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 origin: A 3d point on the plane/Center of the scale

		 input_position: input array of 3d points

		 output_position: output array of 3d points projected on a plane

		 normal: plane normal

		 translation: translation vector 

		 rotation: rotation vector 

		 scale: scale factor

		 matrix: 4x4 affine matrix

		 method: transformation method either translation or scale or rotation or random or projectOnPlane

		 seedValue: the seed value for the random generator

		 maxRandomDisplacement: the maximum displacement around initial position for the random transformation

		 fixedIndices: Indices of the entries that are not transformed

		 filename: filename of an affine matrix. Supported extensions are: .trm, .tfm, .xfm and .txt(read as .xfm)

		 drawInput: Draw input points

		 drawOutput: Draw output points

		 pointSize: Point size


    """
    return attachedTo.createObject("TransformPosition" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, origin=origin, input_position=input_position, output_position=output_position, normal=normal, translation=translation, rotation=rotation, scale=scale, matrix=matrix, method=method, seedValue=seedValue, maxRandomDisplacement=maxRandomDisplacement, fixedIndices=fixedIndices, filename=filename, drawInput=drawInput, drawOutput=drawOutput, pointSize=pointSize, **kwargs)
