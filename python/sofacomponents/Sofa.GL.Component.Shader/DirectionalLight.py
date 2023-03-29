# -*- coding: utf-8 -*-


"""
Component DirectionalLight

.. autofunction:: DirectionalLight

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DirectionalLight(attachedTo , name='DirectionalLight', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, color=array([1., 1., 1., 1.], dtype=float32), shadowTextureSize=0, drawSource=0, zNear=0.0, zFar=0.0, shadowsEnabled=1, softShadows=0, shadowFactor=1.0, VSMLightBleeding=0.05000000074505806, VSMMinVariance=0.0010000000474974513, textureUnit=1, modelViewMatrix=array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), projectionMatrix=array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
      dtype=float32), direction=array([ 0.,  0., -1.]), **kwargs):
    """A directional light illuminating the scene with parallel rays of light (can cast shadows).


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

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

		 direction: Set the direction of the light


    """
    return attachedTo.createObject("DirectionalLight" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, color=color, shadowTextureSize=shadowTextureSize, drawSource=drawSource, zNear=zNear, zFar=zFar, shadowsEnabled=shadowsEnabled, softShadows=softShadows, shadowFactor=shadowFactor, VSMLightBleeding=VSMLightBleeding, VSMMinVariance=VSMMinVariance, textureUnit=textureUnit, modelViewMatrix=modelViewMatrix, projectionMatrix=projectionMatrix, direction=direction, **kwargs)
