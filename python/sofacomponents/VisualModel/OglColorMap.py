# -*- coding: utf-8 -*-


"""
Component OglColorMap

.. autofunction:: OglColorMap

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglColorMap(attachedTo , name='OglColorMap', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, paletteSize=256, colorScheme='HSV', showLegend=0, legendOffset=[[10.0, 5.0]], legendTitle='', min=0.0, max=0.0, legendRangeScale=1.0, **kwargs):
    """Provides color palette and support for conversion of numbers to colors.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 paletteSize: How many colors to use

		 colorScheme: Color scheme to use

		 showLegend: Activate rendering of color scale legend on the side

		 legendOffset: Draw the legend on screen with an x,y offset

		 legendTitle: Add a title to the legend

		 min: min value for drawing the legend without the need to actually use the range with getEvaluator method wich sets the min

		 max: max value for drawing the legend without the need to actually use the range with getEvaluator method wich sets the max

		 legendRangeScale: to change the unit of the min/max value of the legend


    """
    return attachedTo.createObject("OglColorMap" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, paletteSize=paletteSize, colorScheme=colorScheme, showLegend=showLegend, legendOffset=legendOffset, legendTitle=legendTitle, min=min, max=max, legendRangeScale=legendRangeScale, **kwargs)
