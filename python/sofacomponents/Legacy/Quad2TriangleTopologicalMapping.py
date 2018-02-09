# -*- coding: utf-8 -*-


"""
Component Quad2TriangleTopologicalMapping

.. autofunction:: Quad2TriangleTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Quad2TriangleTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where QuadSetTopology is converted to TriangleSetTopology


    Args:


    """
    return attachedTo.createObject("Quad2TriangleTopologicalMapping" , **kwargs)
