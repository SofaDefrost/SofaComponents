# -*- coding: utf-8 -*-


"""
Component InterpolationController

.. autofunction:: InterpolationController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def InterpolationController(attachedTo , name='InterpolationController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, handleEventTriggersUpdate=0, evolution=0, period=1.0, alphaMax=1.0, alpha0=0.0, interpValues=[], **kwargs):
    """Interpolates nodes between two meshes


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 handleEventTriggersUpdate: Event handling frequency controls the controller update frequency

		 evolution: O for fixity, 1 for inflation, 2 for deflation

		 period: time to cover all the interpolation positions between original mesh and alpha*(objective mesh), in seconds 

		 alphaMax: bound defining the max interpolation between the origina (alpha=0) and the objectiv (alpha=1) meshes

		 alpha0: alpha value at t=0. (0 < alpha0 < 1)

		 interpValues: values or the interpolation


    """
    return attachedTo.createObject("InterpolationController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, evolution=evolution, period=period, alphaMax=alphaMax, alpha0=alpha0, interpValues=interpValues, **kwargs)
