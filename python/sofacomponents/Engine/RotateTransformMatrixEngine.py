# -*- coding: utf-8 -*-


"""
Component RotateTransformMatrixEngine

.. autofunction:: RotateTransformMatrixEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RotateTransformMatrixEngine(attachedTo , name='RotateTransformMatrixEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inT=[[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]], outT=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], rotation=[[0.0, 0.0, 0.0]], **kwargs):
    """Compose the input transform (if any) with the given rotation


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inT: input transformation if any

		 outT: output transformation

		 rotation: euler angles


    """
    return attachedTo.createObject("RotateTransformMatrixEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inT=inT, outT=outT, rotation=rotation, **kwargs)
