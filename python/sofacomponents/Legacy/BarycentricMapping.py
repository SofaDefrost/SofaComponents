# -*- coding: utf-8 -*-


"""
Component BarycentricMapping

.. autofunction:: BarycentricMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BarycentricMapping(attachedTo , **kwargs):
    """Mapping using barycentric coordinates of the child with respect to cells of its parent


    Args:


    """
    return attachedTo.createObject("BarycentricMapping" , **kwargs)
