# -*- coding: utf-8 -*-


"""
Component QuadBendingSprings

.. autofunction:: QuadBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def QuadBendingSprings(attachedTo , **kwargs):
    """Springs added to a quad mesh to prevent bending


    Args:


    """
    return attachedTo.createObject("QuadBendingSprings" , **kwargs)
