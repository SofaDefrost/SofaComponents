# -*- coding: utf-8 -*-


"""
Component TriangleSetTopologyModifier

.. autofunction:: TriangleSetTopologyModifier

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangleSetTopologyModifier(attachedTo , name='TriangleSetTopologyModifier', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, list_Out=[], **kwargs):
    """Triangle set topology modifier


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 list_Out: triangles with at least one null values.


    """
    return attachedTo.createObject("TriangleSetTopologyModifier" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, list_Out=list_Out, **kwargs)
