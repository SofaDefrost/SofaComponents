# -*- coding: utf-8 -*-


"""
Component HexahedronSetTopologyModifier

.. autofunction:: HexahedronSetTopologyModifier

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HexahedronSetTopologyModifier(attachedTo , name='HexahedronSetTopologyModifier', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, removeIsolated=1, **kwargs):
    """Hexahedron set topology modifier


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 removeIsolated: remove Isolated dof


    """
    return attachedTo.createObject("HexahedronSetTopologyModifier" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, removeIsolated=removeIsolated, **kwargs)
