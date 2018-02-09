# -*- coding: utf-8 -*-


"""
Component SubsetMultiMapping

.. autofunction:: SubsetMultiMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SubsetMultiMapping(attachedTo , **kwargs):
    """Compute a subset of the input MechanicalObjects according to a dof index list


    Args:


    """
    return attachedTo.createObject("SubsetMultiMapping" , **kwargs)
