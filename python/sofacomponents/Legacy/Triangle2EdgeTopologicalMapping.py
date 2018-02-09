# -*- coding: utf-8 -*-


"""
Component Triangle2EdgeTopologicalMapping

.. autofunction:: Triangle2EdgeTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Triangle2EdgeTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where TriangleSetTopology is converted to EdgeSetTopology


    Args:


    """
    return attachedTo.createObject("Triangle2EdgeTopologicalMapping" , **kwargs)
