# -*- coding: utf-8 -*-


"""
Component LightManager

.. autofunction:: LightManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LightManager(attachedTo , name='LightManager', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, shadows=0, softShadows=0, ambient=array([0., 0., 0., 1.], dtype=float32), debugDraw=0, **kwargs):
    """Manage a set of lights that can cast hard and soft shadows.Soft Shadows is done using Variance Shadow Mapping (http://developer.download.nvidia.com/SDK/10.5/direct3d/Source/VarianceShadowMapping/Doc/VarianceShadowMapping.pdf)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 shadows: Enable Shadow in the scene. (default=0)

		 softShadows: If Shadows enabled, Enable Variance Soft Shadow in the scene. (default=0)

		 ambient: Ambient lights contribution (Vec4f)(default=[0.0f,0.0f,0.0f,0.0f])

		 debugDraw: enable/disable drawing of lights shadow textures. (default=false)


    """
    return attachedTo.createObject("LightManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, shadows=shadows, softShadows=softShadows, ambient=ambient, debugDraw=debugDraw, **kwargs)
