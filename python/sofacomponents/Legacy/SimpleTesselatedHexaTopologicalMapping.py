# -*- coding: utf-8 -*-


"""
Component SimpleTesselatedHexaTopologicalMapping

.. autofunction:: SimpleTesselatedHexaTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SimpleTesselatedHexaTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where HexahedronSetTopology is converted into a finer HexahedronSetTopology


    Args:


    """
    return attachedTo.createObject("SimpleTesselatedHexaTopologicalMapping" , **kwargs)
