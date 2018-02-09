# -*- coding: utf-8 -*-


"""
Component VisualManagerSecondaryPass

.. autofunction:: VisualManagerSecondaryPass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VisualManagerSecondaryPass(attachedTo , name='VisualManagerSecondaryPass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, factor=1.0, renderToScreen=0, outputName='', input_tags=[], output_tags=[], fragFilename='', **kwargs):
    """VisualManagerSecondaryPass


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 factor: set the resolution factor for the output pass. default value:1.0

		 renderToScreen: if true, this pass will be displayed on screen (only one renderPass in the scene must be defined as renderToScreen)

		 outputName: name the output texture

		 input_tags: list of input passes used as source textures

		 output_tags: output reference tag (use it if the resulting fbo is used as a source for another secondary pass)

		 fragFilename: Set the fragment shader filename to load


    """
    return attachedTo.createObject("VisualManagerSecondaryPass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, factor=factor, renderToScreen=renderToScreen, outputName=outputName, input_tags=input_tags, output_tags=output_tags, fragFilename=fragFilename, **kwargs)
