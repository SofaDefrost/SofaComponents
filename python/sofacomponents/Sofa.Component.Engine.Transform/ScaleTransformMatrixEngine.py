# -*- coding: utf-8 -*-


"""
Component ScaleTransformMatrixEngine

.. autofunction:: ScaleTransformMatrixEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ScaleTransformMatrixEngine(attachedTo , name='ScaleTransformMatrixEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, inT=array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]]), outT=array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 1.]]), scale=array([0., 0., 0.]), **kwargs):
    """Compose the input transform (if any) with the given scale transformation


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 inT: input transformation if any

		 outT: output transformation

		 scale: scaling values


    """
    return attachedTo.createObject("ScaleTransformMatrixEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, inT=inT, outT=outT, scale=scale, **kwargs)
