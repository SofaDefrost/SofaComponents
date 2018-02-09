# -*- coding: utf-8 -*-


"""
Component BeamFEMForceField

.. autofunction:: BeamFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BeamFEMForceField(attachedTo , **kwargs):
    """Beam finite elements


    Args:


    """
    return attachedTo.createObject("BeamFEMForceField" , **kwargs)
