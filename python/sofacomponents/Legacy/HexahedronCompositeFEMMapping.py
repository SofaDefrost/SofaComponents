# -*- coding: utf-8 -*-


"""
Component HexahedronCompositeFEMMapping

.. autofunction:: HexahedronCompositeFEMMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HexahedronCompositeFEMMapping(attachedTo , **kwargs):
    """Set the point to the center of mass of the DOFs it is attached to


    Args:


    """
    return attachedTo.createObject("HexahedronCompositeFEMMapping" , **kwargs)
