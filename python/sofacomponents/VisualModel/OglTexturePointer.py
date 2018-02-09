# -*- coding: utf-8 -*-


"""
Component OglTexturePointer

.. autofunction:: OglTexturePointer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglTexturePointer(attachedTo , name='OglTexturePointer', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, id='', indexShader=0, textureUnit=1, enabled=1, **kwargs):
    """OglTexturePointer


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 textureUnit: Set the texture unit

		 enabled: enabled ?


    """
    return attachedTo.createObject("OglTexturePointer" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, id=id, indexShader=indexShader, textureUnit=textureUnit, enabled=enabled, **kwargs)
