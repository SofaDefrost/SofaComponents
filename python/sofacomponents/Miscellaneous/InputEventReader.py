# -*- coding: utf-8 -*-


"""
Component InputEventReader

.. autofunction:: InputEventReader

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def InputEventReader(attachedTo , name='InputEventReader', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, filename='/dev/input/mouse2', inverseSense=0, printEvent=0, key1=48, key2=49, writeEvents=0, outputFilename='', **kwargs):
    """Read events from file


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 filename: input events file name

		 inverseSense: inverse the sense of the mouvement

		 printEvent: Print event informations

		 key1: Key event generated when the left pedal is pressed

		 key2: Key event generated when the right pedal is pressed

		 writeEvents: If true, write incoming events ; if false, read events from that file (if an output filename is provided)

		 outputFilename: Other filename where events will be stored (or read)


    """
    return attachedTo.createObject("InputEventReader" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, inverseSense=inverseSense, printEvent=printEvent, key1=key1, key2=key2, writeEvents=writeEvents, outputFilename=outputFilename, **kwargs)
