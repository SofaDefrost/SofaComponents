# -*- coding: utf-8 -*-


"""
Component Hexa2TetraTopologicalMapping

.. autofunction:: Hexa2TetraTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Hexa2TetraTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where HexahedronSetTopology is converted to TetrahedronSetTopology


    Args:


    """
    return attachedTo.createObject("Hexa2TetraTopologicalMapping" , **kwargs)
