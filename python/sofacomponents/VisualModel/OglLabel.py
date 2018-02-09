# -*- coding: utf-8 -*-


"""
Component OglLabel

.. autofunction:: OglLabel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglLabel(attachedTo , name='OglLabel', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, prefix='', label='', suffix='', x=10, y=10, fontsize=14, color='0.5 0.5 0.5 1', selectContrastingColor=0, updateLabelEveryNbSteps=0, visible=1, **kwargs):
    """Display 2D text in the viewport.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 prefix: The prefix of the text to display

		 label: The text to display

		 suffix: The suffix of the text to display

		 x: The x position of the text on the screen

		 y: The y position of the text on the screen

		 fontsize: The size of the font used to display the text on the screen

		 color: The color of the text to display. (default='gray')

		 selectContrastingColor: Overide the color value but one that contrast with the background color

		 updateLabelEveryNbSteps: Update the display of the label every nb of time steps

		 visible: Is label displayed


    """
    return attachedTo.createObject("OglLabel" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, prefix=prefix, label=label, suffix=suffix, x=x, y=y, fontsize=fontsize, color=color, selectContrastingColor=selectContrastingColor, updateLabelEveryNbSteps=updateLabelEveryNbSteps, visible=visible, **kwargs)
