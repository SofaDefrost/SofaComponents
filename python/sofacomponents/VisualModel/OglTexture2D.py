# -*- coding: utf-8 -*-


"""
Component OglTexture2D

.. autofunction:: OglTexture2D

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglTexture2D(attachedTo , name='OglTexture2D', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, id='', indexShader=0, textureFilename='', textureUnit=1, enabled=1, repeat=0, linearInterpolation=1, generateMipmaps=1, srgbColorspace=0, minLod=-1000.0, maxLod=1000.0, proceduralTextureWidth=0, proceduralTextureHeight=0, proceduralTextureNbBits=1, proceduralTextureData=[], cubemapFilenamePosX='', cubemapFilenamePosY='', cubemapFilenamePosZ='', cubemapFilenameNegX='', cubemapFilenameNegY='', cubemapFilenameNegZ='', texture2DFilename='', **kwargs):
    """OglTexture2D


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 textureFilename: Texture Filename

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

		 texture2DFilename: Texture2D Filename


    """
    return attachedTo.createObject("OglTexture2D" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, id=id, indexShader=indexShader, textureFilename=textureFilename, textureUnit=textureUnit, enabled=enabled, repeat=repeat, linearInterpolation=linearInterpolation, generateMipmaps=generateMipmaps, srgbColorspace=srgbColorspace, minLod=minLod, maxLod=maxLod, proceduralTextureWidth=proceduralTextureWidth, proceduralTextureHeight=proceduralTextureHeight, proceduralTextureNbBits=proceduralTextureNbBits, proceduralTextureData=proceduralTextureData, cubemapFilenamePosX=cubemapFilenamePosX, cubemapFilenamePosY=cubemapFilenamePosY, cubemapFilenamePosZ=cubemapFilenamePosZ, cubemapFilenameNegX=cubemapFilenameNegX, cubemapFilenameNegY=cubemapFilenameNegY, cubemapFilenameNegZ=cubemapFilenameNegZ, texture2DFilename=texture2DFilename, **kwargs)
