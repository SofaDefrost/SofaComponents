# -*- coding: utf-8 -*-


"""
Component IdentityTopologicalMapping

.. autofunction:: IdentityTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def IdentityTopologicalMapping(attachedTo , **kwargs):
    """This class is a specific implementation of TopologicalMapping where the destination topology should be kept identical to the source topology. The implementation currently assumes that both topology have been initialized identically.


    Args:


    """
    return attachedTo.createObject("IdentityTopologicalMapping" , **kwargs)
