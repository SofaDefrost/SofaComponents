# -*- coding: utf-8 -*-


"""
Component ProjectiveTransformEngine

.. autofunction:: ProjectiveTransformEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ProjectiveTransformEngine(attachedTo , name='ProjectiveTransformEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, input_position=[], output_position=[], proj_mat=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], focal_distance=1.0, **kwargs):
    """Project the position of 3d points onto a plane according to a projection matrix


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 input_position: input array of 3d points

		 output_position: output array of projected 3d points

		 proj_mat: projection matrix 

		 focal_distance: focal distance 


    """
    return attachedTo.createObject("ProjectiveTransformEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, input_position=input_position, output_position=output_position, proj_mat=proj_mat, focal_distance=focal_distance, **kwargs)
