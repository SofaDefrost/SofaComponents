# -*- coding: utf-8 -*-


"""
Component OglMatrix3Variable

.. autofunction:: OglMatrix3Variable

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglMatrix3Variable(attachedTo , name='OglMatrix3Variable', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, id='', indexShader=0, value=array([], dtype=float32), transpose=0, **kwargs):
    """OglMatrix3Variable


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 value: Set Uniform Value

		 transpose: Transpose the matrix (e.g. to use row-dominant matrices in OpenGL


    """
    return attachedTo.createObject("OglMatrix3Variable" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, id=id, indexShader=indexShader, value=value, transpose=transpose, **kwargs)
