# -*- coding: utf-8 -*-


"""
Component Edge2QuadTopologicalMapping

.. autofunction:: Edge2QuadTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Edge2QuadTopologicalMapping(attachedTo , **kwargs):
    """Special case of mapping where EdgeSetTopology is converted to QuadSetTopology


    Args:


    """
    return attachedTo.createObject("Edge2QuadTopologicalMapping" , **kwargs)
