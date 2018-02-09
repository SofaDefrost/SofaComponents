# -*- coding: utf-8 -*-


"""
Component EvalPointsDistance

.. autofunction:: EvalPointsDistance

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EvalPointsDistance(attachedTo , name='EvalPointsDistance', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, draw=1, isToPrint=0, filename='', period=0.0, distance=[], distMean=1.0, distMin=1.0, distMax=1.0, distDev=1.0, rdistMean=1.0, rdistMin=1.0, rdistMax=1.0, rdistDev=1.0, **kwargs):
    """Periodically compute the distance between 2 set of points


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 draw: activate rendering of lines between associated points

		 isToPrint: suppress somes data before using save as function

		 filename: output file name

		 period: period between outputs

		 distance: distances (OUTPUT)

		 distMean: mean distance (OUTPUT)

		 distMin: min distance (OUTPUT)

		 distMax: max distance (OUTPUT)

		 distDev: distance standard deviation (OUTPUT)

		 rdistMean: mean relative distance (OUTPUT)

		 rdistMin: min relative distance (OUTPUT)

		 rdistMax: max relative distance (OUTPUT)

		 rdistDev: relative distance standard deviation (OUTPUT)


    """
    return attachedTo.createObject("EvalPointsDistance" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, draw=draw, isToPrint=isToPrint, filename=filename, period=period, distance=distance, distMean=distMean, distMin=distMin, distMax=distMax, distDev=distDev, rdistMean=rdistMean, rdistMin=rdistMin, rdistMax=rdistMax, rdistDev=rdistDev, **kwargs)
