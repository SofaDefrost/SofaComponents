# -*- coding: utf-8 -*-


"""
Component Hexa2QuadTopologicalMapping

.. autofunction:: Hexa2QuadTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Hexa2QuadTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where HexahedronSetTopology is converted to QuadSetTopology


    Args:


    """
    return attachedTo.createObject("Hexa2QuadTopologicalMapping" , **kwargs)
