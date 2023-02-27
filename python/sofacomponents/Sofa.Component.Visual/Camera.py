# -*- coding: utf-8 -*-


"""
Component Camera

.. autofunction:: Camera

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Camera(attachedTo , name='Camera', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, position=array([0., 0., 0.]), orientation=array([0., 0., 0., 1.]), lookAt=array([0., 0., 0.]), distance=0.0, fieldOfView=45.0, zNear=0.01, zFar=100.0, computeZClip=0, minBBox=array([0., 0., 0.]), maxBBox=array([1., 1., 1.]), widthViewport=800, heightViewport=600, projectionType='Perspective', activated=1, fixedLookAt=0, modelViewMatrix=array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), projectionMatrix=array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), **kwargs):
    """A Camera that render the scene from a given location & orientation.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

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


    """
    return attachedTo.createObject("Camera" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, orientation=orientation, lookAt=lookAt, distance=distance, fieldOfView=fieldOfView, zNear=zNear, zFar=zFar, computeZClip=computeZClip, minBBox=minBBox, maxBBox=maxBBox, widthViewport=widthViewport, heightViewport=heightViewport, projectionType=projectionType, activated=activated, fixedLookAt=fixedLookAt, modelViewMatrix=modelViewMatrix, projectionMatrix=projectionMatrix, **kwargs)
