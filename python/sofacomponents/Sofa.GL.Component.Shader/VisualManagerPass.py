# -*- coding: utf-8 -*-


"""
Component VisualManagerPass

.. autofunction:: VisualManagerPass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VisualManagerPass(attachedTo , name='VisualManagerPass', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, factor=1.0, renderToScreen=0, outputName='', **kwargs):
    """VisualManagerPass


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 factor: set the resolution factor for the output pass. default value:1.0

		 renderToScreen: if true, this pass will be displayed on screen (only one renderPass in the scene must be defined as renderToScreen)

		 outputName: name the output texture


    """
    return attachedTo.createObject("VisualManagerPass" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, factor=factor, renderToScreen=renderToScreen, outputName=outputName, **kwargs)
