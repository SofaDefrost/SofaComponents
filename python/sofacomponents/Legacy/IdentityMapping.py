# -*- coding: utf-8 -*-


"""
Component IdentityMapping

.. autofunction:: IdentityMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def IdentityMapping(attachedTo , **kwargs):
    """Special case of mapping where the child points are the same as the parent points


    Args:


    """
    return attachedTo.createObject("IdentityMapping" , **kwargs)
