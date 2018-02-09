# -*- coding: utf-8 -*-


"""
Component SubsetTopologicalMapping

.. autofunction:: SubsetTopologicalMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SubsetTopologicalMapping(attachedTo , **kwargs):
    """This class is a specific implementation of TopologicalMapping where the destination topology is a subset of the source topology. The implementation currently assumes that both topologies have been initialized correctly.


    Args:


    """
    return attachedTo.createObject("SubsetTopologicalMapping" , **kwargs)
