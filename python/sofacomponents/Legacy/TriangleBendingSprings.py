# -*- coding: utf-8 -*-


"""
Component TriangleBendingSprings

.. autofunction:: TriangleBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangleBendingSprings(attachedTo , **kwargs):
    """Springs added to a traingular mesh to prevent bending


    Args:


    """
    return attachedTo.createObject("TriangleBendingSprings" , **kwargs)
