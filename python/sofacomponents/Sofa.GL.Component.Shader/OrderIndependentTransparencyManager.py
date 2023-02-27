# -*- coding: utf-8 -*-


"""
Component OrderIndependentTransparencyManager

.. autofunction:: OrderIndependentTransparencyManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OrderIndependentTransparencyManager(attachedTo , name='OrderIndependentTransparencyManager', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, depthScale=0.009999999776482582, **kwargs):
    """OrderIndependentTransparencyManager


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 depthScale: Depth scale


    """
    return attachedTo.createObject("OrderIndependentTransparencyManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, depthScale=depthScale, **kwargs)
