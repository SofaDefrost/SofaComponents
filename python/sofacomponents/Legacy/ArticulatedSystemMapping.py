# -*- coding: utf-8 -*-


"""
Component ArticulatedSystemMapping

.. autofunction:: ArticulatedSystemMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ArticulatedSystemMapping(attachedTo , **kwargs):
    """Mapping between a set of 6D DOF's and a set of angles (µ) using an articulated hierarchy container. 


    Args:


    """
    return attachedTo.createObject("ArticulatedSystemMapping" , **kwargs)
