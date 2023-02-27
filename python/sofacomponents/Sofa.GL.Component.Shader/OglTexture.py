# -*- coding: utf-8 -*-


"""
Component OglTexture

.. autofunction:: OglTexture

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglTexture(attachedTo , name='OglTexture', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, id='', indexShader=0, filename='', textureUnit=1, enabled=1, repeat=0, linearInterpolation=1, generateMipmaps=1, srgbColorspace=0, minLod=-1000.0, maxLod=1000.0, proceduralTextureWidth=0, proceduralTextureHeight=0, proceduralTextureNbBits=1, proceduralTextureData=array([], dtype=int32), cubemapFilenamePosX='', cubemapFilenamePosY='', cubemapFilenamePosZ='', cubemapFilenameNegX='', cubemapFilenameNegY='', cubemapFilenameNegZ='', **kwargs):
    """OglTexture


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 filename: Texture Filename

		 textureUnit: Set the texture unit

		 enabled: enabled ?

		 repeat: Repeat Texture ?

		 linearInterpolation: Interpolate Texture ?

		 generateMipmaps: Generate mipmaps ?

		 srgbColorspace: SRGB colorspace ?

		 minLod: Minimum mipmap lod ?

		 maxLod: Maximum mipmap lod ?

		 proceduralTextureWidth: Width of procedural Texture

		 proceduralTextureHeight: Height of procedural Texture

		 proceduralTextureNbBits: Nb bits per color

		 proceduralTextureData: Data of procedural Texture 

		 cubemapFilenamePosX: Texture filename of positive-X cubemap face

		 cubemapFilenamePosY: Texture filename of positive-Y cubemap face

		 cubemapFilenamePosZ: Texture filename of positive-Z cubemap face

		 cubemapFilenameNegX: Texture filename of negative-X cubemap face

		 cubemapFilenameNegY: Texture filename of negative-Y cubemap face

		 cubemapFilenameNegZ: Texture filename of negative-Z cubemap face


    """
    return attachedTo.createObject("OglTexture" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, id=id, indexShader=indexShader, filename=filename, textureUnit=textureUnit, enabled=enabled, repeat=repeat, linearInterpolation=linearInterpolation, generateMipmaps=generateMipmaps, srgbColorspace=srgbColorspace, minLod=minLod, maxLod=maxLod, proceduralTextureWidth=proceduralTextureWidth, proceduralTextureHeight=proceduralTextureHeight, proceduralTextureNbBits=proceduralTextureNbBits, proceduralTextureData=proceduralTextureData, cubemapFilenamePosX=cubemapFilenamePosX, cubemapFilenamePosY=cubemapFilenamePosY, cubemapFilenamePosZ=cubemapFilenamePosZ, cubemapFilenameNegX=cubemapFilenameNegX, cubemapFilenameNegY=cubemapFilenameNegY, cubemapFilenameNegZ=cubemapFilenameNegZ, **kwargs)
