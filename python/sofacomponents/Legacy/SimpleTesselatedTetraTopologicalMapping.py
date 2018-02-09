# -*- coding: utf-8 -*-


"""
Component SimpleTesselatedTetraTopologicalMapping

.. autofunction:: SimpleTesselatedTetraTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SimpleTesselatedTetraTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where TetrahedronSetTopology is converted into a finer TetrahedronSetTopology


    Args:


    """
    return attachedTo.createObject("SimpleTesselatedTetraTopologicalMapping" , **kwargs)
