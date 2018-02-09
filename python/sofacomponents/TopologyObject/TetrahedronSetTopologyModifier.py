# -*- coding: utf-8 -*-


"""
Component TetrahedronSetTopologyModifier

.. autofunction:: TetrahedronSetTopologyModifier

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedronSetTopologyModifier(attachedTo , name='TetrahedronSetTopologyModifier', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, list_Out=[], removeIsolated=1, **kwargs):
    """Tetrahedron set topology modifier


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 list_Out: triangles with at least one null values.

		 removeIsolated: remove Isolated dof


    """
    return attachedTo.createObject("TetrahedronSetTopologyModifier" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, list_Out=list_Out, removeIsolated=removeIsolated, **kwargs)
