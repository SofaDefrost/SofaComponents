# -*- coding: utf-8 -*-


"""
Component PositionalLight

.. autofunction:: PositionalLight

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PositionalLight(attachedTo , name='PositionalLight', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, color='1 1 1 1', shadowTextureSize=0, drawSource=0, zNear=0.0, zFar=0.0, shadowsEnabled=1, softShadows=0, shadowFactor=1.0, VSMLightBleeding=0.05000000074505806, VSMMinVariance=0.0010000000474974513, textureUnit=1, modelViewMatrix=[[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]], projectionMatrix=[[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]], fixed=0, position=[[-0.7, 0.3, 0.0]], attenuation=0.0, **kwargs):
    """A positional light illuminating the scene.The light has a location from which the ray are starting in all direction  (cannot cast shadows for now)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 color: Set the color of the light. (default=[1.0,1.0,1.0,1.0])

		 shadowTextureSize: [Shadowing] Set size for shadow texture 

		 drawSource: Draw Light Source

		 zNear: [Shadowing] Light's ZNear

		 zFar: [Shadowing] Light's ZFar

		 shadowsEnabled: [Shadowing] Enable Shadow from this light

		 softShadows: [Shadowing] Turn on Soft Shadow from this light

		 shadowFactor: [Shadowing] Shadow Factor (decrease/increase darkness)

		 VSMLightBleeding: [Shadowing] (VSM only) Light bleeding paramter

		 VSMMinVariance: [Shadowing] (VSM only) Minimum variance parameter

		 textureUnit: [Shadowing] Texture unit for the genereated shadow texture

		 modelViewMatrix: [Shadowing] ModelView Matrix

		 projectionMatrix: [Shadowing] Projection Matrix

		 fixed: Fix light position from the camera

		 position: Set the position of the light

		 attenuation: Set the attenuation of the light


    """
    return attachedTo.createObject("PositionalLight" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, color=color, shadowTextureSize=shadowTextureSize, drawSource=drawSource, zNear=zNear, zFar=zFar, shadowsEnabled=shadowsEnabled, softShadows=softShadows, shadowFactor=shadowFactor, VSMLightBleeding=VSMLightBleeding, VSMMinVariance=VSMMinVariance, textureUnit=textureUnit, modelViewMatrix=modelViewMatrix, projectionMatrix=projectionMatrix, fixed=fixed, position=position, attenuation=attenuation, **kwargs)
