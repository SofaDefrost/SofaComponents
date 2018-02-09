# -*- coding: utf-8 -*-


"""
Component InteractiveCamera

.. autofunction:: InteractiveCamera

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def InteractiveCamera(attachedTo , name='InteractiveCamera', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, position=[[0.0, 0.0, 0.0]], orientation=[[0.0, 0.0, 0.0, 1.0]], lookAt=[[0.0, 0.0, 0.0]], distance=0.0, fieldOfView=45.0, zNear=0.0, zFar=0.0, computeZClip=1, minBBox=[[0.0, 0.0, 0.0]], maxBBox=[[1.0, 1.0, 1.0]], widthViewport=800, heightViewport=600, projectionType='Perspective', activated=1, fixedLookAt=0, modelViewMatrix=[[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]], projectionMatrix=[[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]], zoomSpeed=250.0, panSpeed=0.1, pivot=2, **kwargs):
    """InteractiveCamera


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: Camera's position

		 orientation: Camera's orientation

		 lookAt: Camera's look at

		 distance: Distance between camera and look at

		 fieldOfView: Camera's FOV

		 zNear: Camera's zNear

		 zFar: Camera's zFar

		 computeZClip: Compute Z clip planes (Near and Far) according to the bounding box

		 minBBox: minBBox

		 maxBBox: maxBBox

		 widthViewport: widthViewport

		 heightViewport: heightViewport

		 projectionType: Camera Type (0 = Perspective, 1 = Orthographic)

		 activated: Camera activated ?

		 fixedLookAt: keep the lookAt point always fixed

		 modelViewMatrix: ModelView Matrix

		 projectionMatrix: Projection Matrix

		 zoomSpeed: Zoom Speed

		 panSpeed: Pan Speed

		 pivot: Pivot (0 => Camera lookAt, 1 => Camera position, 2 => Scene center, 3 => World center


    """
    return attachedTo.createObject("InteractiveCamera" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, orientation=orientation, lookAt=lookAt, distance=distance, fieldOfView=fieldOfView, zNear=zNear, zFar=zFar, computeZClip=computeZClip, minBBox=minBBox, maxBBox=maxBBox, widthViewport=widthViewport, heightViewport=heightViewport, projectionType=projectionType, activated=activated, fixedLookAt=fixedLookAt, modelViewMatrix=modelViewMatrix, projectionMatrix=projectionMatrix, zoomSpeed=zoomSpeed, panSpeed=panSpeed, pivot=pivot, **kwargs)
