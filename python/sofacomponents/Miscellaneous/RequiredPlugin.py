# -*- coding: utf-8 -*-


"""
Component RequiredPlugin

.. autofunction:: RequiredPlugin

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RequiredPlugin(attachedTo , name='RequiredPlugin', printLog=1, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, pluginName=[['RequiredPlugin']], suffixMap=[], stopAfterFirstNameFound=0, stopAfterFirstSuffixFound=1, requireOne=0, requireAll=1, **kwargs):
    """Load the required plugins


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 pluginName: plugin name (or several names if you need to load different plugins or a plugin with several alternate names)

		 suffixMap: standard->custom suffixes pairs (to be used if the plugin is compiled outside of Sofa with a non standard way of differenciating versions), using ! to represent empty suffix

		 stopAfterFirstNameFound: Stop after the first plugin name that is loaded successfully

		 stopAfterFirstSuffixFound: For each plugin name, stop after the first suffix that is loaded successfully

		 requireOne: Display an error message if no plugin names were successfully loaded

		 requireAll: Display an error message if any plugin names failed to be loaded


    """
    return attachedTo.createObject("RequiredPlugin" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, pluginName=pluginName, suffixMap=suffixMap, stopAfterFirstNameFound=stopAfterFirstNameFound, stopAfterFirstSuffixFound=stopAfterFirstSuffixFound, requireOne=requireOne, requireAll=requireAll, **kwargs)
