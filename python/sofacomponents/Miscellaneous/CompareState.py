# -*- coding: utf-8 -*-


"""
Component CompareState

.. autofunction:: CompareState

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CompareState(attachedTo , name='CompareState', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, filename='', interval=0.0, shift=0.0, loop=0, scalePos=1.0, **kwargs):
    """Compare State vectors from a reference frame to the associated Mechanical State


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
    return attachedTo.createObject("CompareState" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, interval=interval, shift=shift, loop=loop, scalePos=scalePos, **kwargs)
