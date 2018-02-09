# -*- coding: utf-8 -*-


"""
Component PointSetTopologyModifier

.. autofunction:: PointSetTopologyModifier

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PointSetTopologyModifier(attachedTo , name='PointSetTopologyModifier', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, **kwargs):
    """Point set topology modifier


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("PointSetTopologyModifier" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, **kwargs)
