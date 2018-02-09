# -*- coding: utf-8 -*-


"""
Component IdentityMultiMapping

.. autofunction:: IdentityMultiMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def IdentityMultiMapping(attachedTo , **kwargs):
    """Concatenate several States together


    Args:


    """
    return attachedTo.createObject("IdentityMultiMapping" , **kwargs)
