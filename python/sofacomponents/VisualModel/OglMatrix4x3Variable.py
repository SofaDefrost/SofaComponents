# -*- coding: utf-8 -*-


"""
Component OglMatrix4x3Variable

.. autofunction:: OglMatrix4x3Variable

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglMatrix4x3Variable(attachedTo , name='OglMatrix4x3Variable', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, id='', indexShader=0, value=[], transpose=0, **kwargs):
    """OglMatrix4x3Variable


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 value: Set Uniform Value

		 transpose: Transpose the matrix (e.g. to use row-dominant matrices in OpenGL


    """
    return attachedTo.createObject("OglMatrix4x3Variable" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, id=id, indexShader=indexShader, value=value, transpose=transpose, **kwargs)
