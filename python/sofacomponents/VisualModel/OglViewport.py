# -*- coding: utf-8 -*-


"""
Component OglViewport

.. autofunction:: OglViewport

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglViewport(attachedTo , name='OglViewport', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, screenPosition=[[0, 0]], screenSize=[[0, 0]], cameraPosition=[[0.0, 0.0, 0.0]], cameraOrientation=[[0.0, 0.0, 0.0, 1.0]], cameraRigid=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], zNear=0.0, zFar=0.0, fovy=60.0, enabled=1, advancedRendering=0, useFBO=1, swapMainView=0, drawCamera=0, **kwargs):
    """OglViewport


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 screenPosition: Viewport position

		 screenSize: Viewport size

		 cameraPosition: Camera's position in eye's space

		 cameraOrientation: Camera's orientation

		 cameraRigid: Camera's rigid coord

		 zNear: Camera's ZNear

		 zFar: Camera's ZFar

		 fovy: Field of View (Y axis)

		 enabled: Enable visibility of the viewport

		 advancedRendering: If true, viewport will be hidden if advancedRendering visual flag is not enabled

		 useFBO: Use a FBO to render the viewport

		 swapMainView: Swap this viewport with the main view

		 drawCamera: Draw a frame representing the camera (see it in main viewport)


    """
    return attachedTo.createObject("OglViewport" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, screenPosition=screenPosition, screenSize=screenSize, cameraPosition=cameraPosition, cameraOrientation=cameraOrientation, cameraRigid=cameraRigid, zNear=zNear, zFar=zFar, fovy=fovy, enabled=enabled, advancedRendering=advancedRendering, useFBO=useFBO, swapMainView=swapMainView, drawCamera=drawCamera, **kwargs)
