# -*- coding: utf-8 -*-


"""
Component SofaDefaultPathSetting

.. autofunction:: SofaDefaultPathSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SofaDefaultPathSetting(attachedTo , name='SofaDefaultPathSetting', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, recordPath='', gnuplotPath='', **kwargs):
    """Default Paths for Sofa Application


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 recordPath: Path where will be saved the data of the recorded simulation

		 gnuplotPath: Path where will be saved the gnuplot files


    """
    return attachedTo.createObject("SofaDefaultPathSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, recordPath=recordPath, gnuplotPath=gnuplotPath, **kwargs)
