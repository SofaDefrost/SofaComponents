# -*- coding: utf-8 -*-


"""
Component Tetra2TriangleTopologicalMapping

.. autofunction:: Tetra2TriangleTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Tetra2TriangleTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where TetrahedronSetTopology is converted to TriangleSetTopology


    Args:


    """
    return attachedTo.createObject("Tetra2TriangleTopologicalMapping" , **kwargs)
