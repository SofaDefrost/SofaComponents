# -*- coding: utf-8 -*-


"""
Component OglSceneFrame

.. autofunction:: OglSceneFrame

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglSceneFrame(attachedTo , name='OglSceneFrame', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, draw=1, style='Cylinders', alignment='BottomRight', viewportSize=150, **kwargs):
    """Display a frame at the corner of the scene view


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 draw: Display the frame or not

		 style: Style of the frame

		 alignment: Alignment of the frame in the view

		 viewportSize: Size of the viewport where the frame is rendered


    """
    return attachedTo.createObject("OglSceneFrame" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, draw=draw, style=style, alignment=alignment, viewportSize=viewportSize, **kwargs)
