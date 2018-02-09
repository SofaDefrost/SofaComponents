# -*- coding: utf-8 -*-


"""
Component ReadState

.. autofunction:: ReadState

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ReadState(attachedTo , name='ReadState', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, filename='', interval=0.0, shift=0.0, loop=0, scalePos=1.0, **kwargs):
    """Read State vectors from file at each timestep


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 filename: output file name

		 interval: time duration between inputs

		 shift: shift between times in the file and times when they will be read

		 loop: set to 'true' to re-read the file when reaching the end

		 scalePos: scale the input mechanical object


    """
    return attachedTo.createObject("ReadState" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, interval=interval, shift=shift, loop=loop, scalePos=scalePos, **kwargs)
