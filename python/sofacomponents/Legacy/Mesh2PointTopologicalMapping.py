# -*- coding: utf-8 -*-


"""
Component Mesh2PointTopologicalMapping

.. autofunction:: Mesh2PointTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Mesh2PointTopologicalMapping(attachedTo , **kwargs):
    """This class maps any mesh primitive (point, edge, triangle...) into a point using a relative position from the primitive


    Args:


    """
    return attachedTo.createObject("Mesh2PointTopologicalMapping" , **kwargs)
